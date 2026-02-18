import csv
try:
    import requests
except Exception:
    requests = None

from urllib import request as _request
from urllib.error import URLError
import json

JSONPLACEHOLDER_POSTS = "https://jsonplaceholder.typicode.com/posts"


def _get_posts():
    """Return (status_code, posts_list or None). Uses requests if available, else urllib."""
    if requests is not None:
        try:
            resp = requests.get(JSONPLACEHOLDER_POSTS, timeout=10)
        except requests.RequestException:
            return 0, None
        if not resp.ok:
            return resp.status_code, None
        try:
            return resp.status_code, resp.json()
        except ValueError:
            return resp.status_code, None

    # fallback to urllib
    try:
        with _request.urlopen(JSONPLACEHOLDER_POSTS, timeout=10) as resp:
            raw = resp.read()
            try:
                data = json.loads(raw.decode("utf-8"))
            except ValueError:
                return resp.getcode(), None
            return resp.getcode(), data
    except URLError:
        return 0, None


def fetch_and_print_posts():
    """Fetch posts and print status code and titles."""
    status, posts = _get_posts()
    print(f"Status Code: {status}")
    if not posts:
        return
    for post in posts:
        title = post.get("title")
        if title is not None:
            print(title)


def fetch_and_save_posts(csv_path="posts.csv"):
    """Fetch posts and save id, title, body into a CSV file."""
    status, posts = _get_posts()
    if not posts:
        return

    rows = []
    for post in posts:
        rows.append({
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        })

    fieldnames = ["id", "title", "body"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
