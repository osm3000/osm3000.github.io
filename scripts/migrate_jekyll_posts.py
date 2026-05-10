from __future__ import annotations

import os
import re
import shutil
from datetime import date, datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
QUARTO_CONFIG = ROOT / "_quarto.yml"
GITIGNORE_FILE = ROOT / ".gitignore"
GITIGNORE_DRAFTS_START = "# quarto-migration draft posts"
GITIGNORE_DRAFTS_END = "# /quarto-migration draft posts"


def find_source_root() -> Path:
    configured_root = os.environ.get("JEKYLL_SOURCE_ROOT")
    if configured_root:
        source_root = Path(configured_root).expanduser().resolve()
        if (source_root / "_posts").exists():
            return source_root
        raise FileNotFoundError(f"Configured JEKYLL_SOURCE_ROOT has no _posts directory: {source_root}")

    direct_parent = ROOT.parent
    if (direct_parent / "_posts").exists():
        return direct_parent

    backup_candidates = sorted(
        path for path in ROOT.parent.glob(f"{ROOT.name}-backup-*") if (path / "_posts").exists()
    )
    if backup_candidates:
        return backup_candidates[-1]

    raise FileNotFoundError(
        "Could not find a Jekyll source directory. Set JEKYLL_SOURCE_ROOT or place a sibling backup next to the Quarto site."
    )


SOURCE_ROOT = find_source_root()
SOURCE_POSTS = SOURCE_ROOT / "_posts"
SOURCE_PAGES = SOURCE_ROOT / "pages"
SOURCE_LOGS = SOURCE_ROOT / "_logsfiles"
SOURCE_404 = SOURCE_ROOT / "404.html"
SOURCE_CNAME = SOURCE_ROOT / "CNAME"
SOURCE_FAVICON = SOURCE_ROOT / "favicon.ico"
TARGET_POSTS = ROOT / "posts"
TARGET_LOGS = ROOT / "logs"
SOURCE_ASSETS = SOURCE_ROOT / "assets"
TARGET_ASSETS = ROOT / "assets"
TARGET_CNAME = ROOT / "CNAME"
TARGET_FAVICON = ROOT / "favicon.ico"
FRONT_MATTER_BOUNDARY = "---"
INVALID_FILENAME_CHARS = re.compile(r"[^A-Za-z0-9._-]+")
POST_URL_PATTERN = re.compile(r"\{\%\s*post_url\s+([^\s%]+)\s*\%\}")
POST_FILENAME_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)$")
PAGE_TARGETS = {
    "about.markdown": "about.qmd",
    "phd-work.markdown": "phd-work.qmd",
    "alife.markdown": "alife.qmd",
}
SITE_DESCRIPTION = "I wander the digital universe, seeking the beauty in systems and patterns"


def sanitize_filename(path: Path) -> str:
    stem = INVALID_FILENAME_CHARS.sub("-", path.stem).strip(".-")
    stem = re.sub(r"-+", "-", stem)
    return f"{stem or 'post'}.qmd"


def post_slug(path: Path) -> str:
    match = POST_FILENAME_PATTERN.match(path.stem)
    stem = match.group(1) if match else path.stem
    stem = INVALID_FILENAME_CHARS.sub("-", stem).strip(".-")
    stem = re.sub(r"-+", "-", stem)
    return stem or "post"


def normalize_sequence(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [item for item in value.split() if item]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()]


def dedupe_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    deduped: list[str] = []
    for value in values:
        key = value.casefold()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(value)
    return deduped


def normalize_date(value: object) -> str:
    if isinstance(value, datetime):
        if value.tzinfo is not None:
            return value.strftime("%Y-%m-%d %H:%M:%S %z")
        return value.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(value, date):
        return value.isoformat()
    return str(value)


def date_parts(value: object, fallback_stem: str) -> tuple[str, str, str]:
    normalized = normalize_date(value) if value is not None else fallback_stem[:10]
    candidate = normalized[:10]
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", candidate):
        year, month, day = candidate.split("-")
        return year, month, day

    fallback = fallback_stem[:10]
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", fallback):
        year, month, day = fallback.split("-")
        return year, month, day

    raise ValueError(f"Unable to determine date parts for {fallback_stem}")


def split_front_matter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith(f"{FRONT_MATTER_BOUNDARY}\n"):
        return {}, text

    parts = text.split(FRONT_MATTER_BOUNDARY, 2)
    if len(parts) < 3:
        return {}, text

    raw_front_matter = parts[1]
    body = parts[2].lstrip("\n")
    data = yaml.safe_load(raw_front_matter) or {}
    return data, body


def transform_front_matter(metadata: dict[str, object]) -> dict[str, object]:
    transformed: dict[str, object] = {}

    if "title" in metadata:
        transformed["title"] = str(metadata["title"])

    if "date" in metadata:
        transformed["date"] = metadata["date"]

    description = metadata.get("description") or metadata.get("excerpt")
    if isinstance(description, str) and description.strip():
        transformed["description"] = description.strip()

    categories = normalize_sequence(metadata.get("categories"))
    if categories:
        transformed["categories"] = dedupe_preserve_order(categories)

    tags = normalize_sequence(metadata.get("tags"))
    if tags:
        transformed["tags"] = dedupe_preserve_order(tags)

    published = metadata.get("published")
    if published is False:
        transformed["draft"] = True

    for key, value in metadata.items():
        if key in {
            "layout",
            "excerpt",
            "published",
            "description",
            "categories",
            "tags",
            "title",
            "date",
            "permalink",
            "comments",
        }:
            continue
        transformed[key] = value

    if "date" in transformed:
        transformed["date"] = normalize_date(transformed["date"])

    return transformed


def dump_document(metadata: dict[str, object], body: str) -> str:
    yaml_text = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True).strip()
    return f"{FRONT_MATTER_BOUNDARY}\n{yaml_text}\n{FRONT_MATTER_BOUNDARY}\n{body.rstrip()}\n"


def rewrite_jekyll_links(body: str, path_map: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        slug = match.group(1)
        return path_map.get(slug, f"{slug}.qmd")

    return POST_URL_PATTERN.sub(replace, body)


def canonical_post_html_path(source_path: Path, metadata: dict[str, object]) -> str:
    year, month, day = date_parts(metadata.get("date"), source_path.stem)
    categories = normalize_sequence(metadata.get("categories"))
    parts = [*categories, year, month, day, f"{post_slug(source_path)}.html"]
    return "/" + "/".join(parts)


def dated_post_html_path(source_path: Path, metadata: dict[str, object]) -> str:
    year, month, day = date_parts(metadata.get("date"), source_path.stem)
    return f"/{year}/{month}/{day}/{post_slug(source_path)}.html"


def redirect_aliases(source_path: Path, metadata: dict[str, object]) -> list[str]:
    aliases = [canonical_post_html_path(source_path, metadata), dated_post_html_path(source_path, metadata)]
    deduped_aliases: list[str] = []
    seen: set[str] = set()
    for alias in aliases:
        if alias in seen:
            continue
        seen.add(alias)
        deduped_aliases.append(alias)
    return deduped_aliases


def unified_post_html_path(source_path: Path) -> str:
    return f"/posts/{sanitize_filename(source_path).removesuffix('.qmd')}.html"


def write_document(target_path: Path, metadata: dict[str, object], body: str) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(dump_document(metadata, body), encoding="utf-8")


def migrate_pages(path_map: dict[str, str]) -> None:
    for source_name, target_name in PAGE_TARGETS.items():
        source_path = SOURCE_PAGES / source_name
        metadata, body = split_front_matter(source_path.read_text(encoding="utf-8"))
        write_document(
            ROOT / target_name,
            transform_front_matter(metadata),
            rewrite_jekyll_links(body, path_map),
        )


def migrate_404_page() -> None:
    metadata, body = split_front_matter(SOURCE_404.read_text(encoding="utf-8"))
    transformed = transform_front_matter(metadata)
    transformed.setdefault("title", "404")
    write_document(ROOT / "404.qmd", transformed, body)


def migrate_index() -> None:
    index_metadata: dict[str, object] = {
        "title": "Blog",
        "listing": {
            "contents": "posts",
            "sort": "date desc",
            "type": "default",
            "fields": ["title", "date", "description"],
            "categories": True,
            "sort-ui": False,
            "filter-ui": True,
            "feed": {
                "title": "Exploring the digital universe",
                "description": SITE_DESCRIPTION,
                "type": "partial",
            },
        },
    }
    write_document(ROOT / "index.qmd", index_metadata, SITE_DESCRIPTION)


def migrate_logs() -> None:
    if TARGET_LOGS.exists():
        shutil.rmtree(TARGET_LOGS)
    TARGET_LOGS.mkdir(parents=True, exist_ok=True)

    for source_path in sorted(SOURCE_LOGS.iterdir()):
        if not source_path.is_file() or source_path.name.startswith(".") or source_path.suffix.lower() not in {".md", ".markdown"}:
            continue

        metadata, body = split_front_matter(source_path.read_text(encoding="utf-8"))
        target_name = sanitize_filename(source_path)
        write_document(TARGET_LOGS / target_name, transform_front_matter(metadata), body)

    logbook_body = "A series of logs about my work. Hopefully on daily bases."
    logbook_metadata: dict[str, object] = {
        "title": "Logbook",
        "listing": {
            "contents": "logs",
            "sort": False,
            "type": "default",
            "fields": ["title"],
            "sort-ui": False,
            "filter-ui": False,
        },
    }
    write_document(ROOT / "logbook.qmd", logbook_metadata, logbook_body)


def copy_assets() -> None:
    if TARGET_ASSETS.exists():
        shutil.rmtree(TARGET_ASSETS)
    if SOURCE_ASSETS.exists():
        shutil.copytree(SOURCE_ASSETS, TARGET_ASSETS)


def copy_site_artifacts() -> None:
    if SOURCE_CNAME.exists():
        shutil.copy2(SOURCE_CNAME, TARGET_CNAME)
    if SOURCE_FAVICON.exists():
        shutil.copy2(SOURCE_FAVICON, TARGET_FAVICON)


def sync_quarto_render(draft_paths: list[str]) -> None:
    config = yaml.safe_load(QUARTO_CONFIG.read_text(encoding="utf-8")) or {}
    project = config.setdefault("project", {})
    render_targets = ["*.qmd", "posts/*.qmd", "logs/*.qmd"]
    render_targets.extend(f"!{draft_path}" for draft_path in draft_paths)
    project["render"] = render_targets
    QUARTO_CONFIG.write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def sync_gitignore_drafts(draft_paths: list[str]) -> None:
    lines = GITIGNORE_FILE.read_text(encoding="utf-8").splitlines()
    filtered_lines: list[str] = []
    skip_block = False

    for line in lines:
        if line == GITIGNORE_DRAFTS_START:
            skip_block = True
            continue
        if line == GITIGNORE_DRAFTS_END:
            skip_block = False
            continue
        if not skip_block:
            filtered_lines.append(line)

    while filtered_lines and filtered_lines[-1] == "":
        filtered_lines.pop()

    if draft_paths:
        filtered_lines.append("")
        filtered_lines.append(GITIGNORE_DRAFTS_START)
        filtered_lines.extend(draft_paths)
        filtered_lines.append(GITIGNORE_DRAFTS_END)

    GITIGNORE_FILE.write_text("\n".join(filtered_lines) + "\n", encoding="utf-8")


def migrate_posts() -> None:
    source_paths = [
        source_path
        for source_path in sorted(SOURCE_POSTS.iterdir())
        if source_path.is_file()
        and not source_path.name.startswith(".")
        and source_path.suffix.lower() in {".md", ".markdown"}
    ]
    if TARGET_POSTS.exists():
        shutil.rmtree(TARGET_POSTS)
    TARGET_POSTS.mkdir(parents=True, exist_ok=True)

    top_level_targets: set[Path] = set()
    for source_path in source_paths:
        metadata, _ = split_front_matter(source_path.read_text(encoding="utf-8"))
        top_level_targets.add(Path(canonical_post_html_path(source_path, metadata).lstrip("/")).parts[0])

    for top_level_target in top_level_targets:
        target_path = ROOT / top_level_target
        if target_path.exists() and target_path.is_dir():
            shutil.rmtree(target_path)

    path_map = {
        source_path.stem: unified_post_html_path(source_path)
        for source_path in source_paths
    }
    draft_paths: list[str] = []

    for source_path in source_paths:
        metadata, body = split_front_matter(source_path.read_text(encoding="utf-8"))
        transformed = transform_front_matter(metadata)
        transformed["aliases"] = redirect_aliases(source_path, metadata)
        target_path = TARGET_POSTS / sanitize_filename(source_path)
        if transformed.get("draft") is True:
            draft_paths.append(target_path.relative_to(ROOT).as_posix())
        write_document(
            target_path,
            transformed,
            rewrite_jekyll_links(body, path_map),
        )

    migrate_index()
    migrate_pages(path_map)
    migrate_404_page()
    migrate_logs()
    copy_assets()
    copy_site_artifacts()
    sync_quarto_render(draft_paths)
    sync_gitignore_drafts(draft_paths)


if __name__ == "__main__":
    migrate_posts()