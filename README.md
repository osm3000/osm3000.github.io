# New Website

This folder contains a minimal Quarto website scaffold and a migrated copy of the current Jekyll blog content.

## Setup

```bash
poetry install
poetry run python scripts/migrate_jekyll_posts.py
quarto preview
```

The migration script:

- copies `_posts/` into Quarto-native `.qmd` files under `posts/`
- migrates the main static pages (`about`, `phd-work`, `alife`)
- migrates the top-level `404.html` page into Quarto
- migrates `_logsfiles/` into Quarto pages under `logs/`
- creates a Quarto logbook index page
- converts Jekyll metadata into Quarto-friendly front matter
- rewrites Jekyll post link references into Quarto-friendly paths
- copies the current `assets/` directory into this project
- copies the existing `favicon.ico` and `CNAME` files for GitHub Pages deployment

The generated blog index also publishes an RSS feed, and the site reuses the existing Google Analytics measurement ID from the Jekyll configuration.
