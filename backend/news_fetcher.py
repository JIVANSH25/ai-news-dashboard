import feedparser

def fetch_news():
    feeds = [
        "https://techcrunch.com/tag/artificial-intelligence/feed/",
        "https://openai.com/blog/rss.xml"
    ]

    all_news = []

    for url in feeds:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            news = {
                "title": entry.title,
                "summary": entry.summary if "summary" in entry else "",
                "link": entry.link,
                "published": entry.published if "published" in entry else ""
            }
            all_news.append(news)

    return all_news 