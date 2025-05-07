from feedgen.feed import FeedGenerator
from datetime import datetime
import os
from datetime import timezone

def create_rss_feed(title, description, link, language="en", output_file="selfhood.xml"):
    fg = FeedGenerator()
    fg.title(title)
    fg.description(description)
    fg.link(href=link)
    fg.language(language)
    fg.lastBuildDate(datetime.now(timezone.utc))
    return fg

def add_entry(fg, title, description, link, pub_date=None):
    fe = fg.add_entry()
    fe.title(title)
    fe.description(description)
    fe.link(href=link)
    if pub_date:
        if pub_date.tzinfo is None:
            pub_date = pub_date.replace(tzinfo=timezone.utc)
        fe.published(pub_date)
    else:
        fe.published(datetime.now(timezone.utc))
    return fg

def save_feed(fg, output_file="selfhood.xml"):
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fg.rss_file(output_file)
    print(f"RSS feed saved to {output_file}")

def main():
    fg = create_rss_feed(
        title="Selfhood",
        description="Exploring the journey of self-discovery",
        link="https://example.com",
        language="en"
    )
    add_entry(
        fg,
        title="First Post",
        description="This is my first blog post",
        link="https://example.com/post1"
    )
    add_entry(
        fg,
        title="Second Post",
        description="This is my second blog post",
        link="https://example.com/post2"
    )
    save_feed(fg)

if __name__ == "__main__":
    main()
