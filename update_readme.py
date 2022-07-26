import time
import shutil
import feedparser

RSS_URL = "https://vanslog.io/index.xml"
RSS_FEED = feedparser.parse(RSS_URL)
POST_NUM = 5

def main():
    shutil.copyfile('profile.md', 'README.md')
    with open("README.md", 'a', encoding='utf-8') as f:
        f.write(load_latest_posts())

def load_latest_posts() -> str:
    latest_posts = ""
    for idx, feed in enumerate(RSS_FEED['entries']):
        if idx >= POST_NUM:
            break
        feed_date = feed['published_parsed']
        latest_posts += f"- [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']})\n"
    return latest_posts

if __name__ == "__main__":
    main()
