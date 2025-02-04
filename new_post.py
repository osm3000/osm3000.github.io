import click
import datetime

@click.command()
@click.option("--title", prompt="The post title", help="Write the title of the post")
@click.option("--tags", prompt="The post tags", help="Write the tags of the post")
def create_new_post(title, tags):
    """
    Create a new empty post for Jekyll blog in the _posts directory, with the correct filename format and the YAML front matter.
    For date inside the YAML front matter, it will use the current date, similar format to 2025-01-05 00:00:00 +0100
    """
    today = datetime.date.today()
    filename = f"_posts/{today}-{title.lower().replace(' ', '-')}.md"

    # today = today.strftime("%Y-%m-%d %H:%M:%S +0100")
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S +0100")

    # Prompt for the tags
    tags = tags.split(",")
    tags = [tag.strip() for tag in tags]
    tags = ", ".join(tags)


    with open(filename, "w") as file:
        file.write(
            f"---\n"
            f"layout: post\n"
            f"title: {title}\n"
            f"date: {today}\n"
            f"tags: [{tags}]\n"
            f"excerpt: \n"
            f"published: false\n"
            f"---\n"
        )
    click.echo(f"Created new post: {filename}")
    click.launch(filename)


if __name__ == "__main__":
    click.clear()
    create_new_post()
