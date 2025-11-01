import praw
import pandas as pd
from datetime import datetime
from langdetect import detect, DetectorFactory
import os

# Ensure consistent language detection
DetectorFactory.seed = 0

# Function to check if text is Slovenian
def is_slovenian(text):
    try:
        return detect(text) == "sl"
    except:
        return False

# Reddit API credentials
# Replace with your own Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="scraper by u/test1"
)

# Subreddit to scrape
subreddit_name = "Ljubljana"
subreddit = reddit.subreddit(subreddit_name)

# Fetch posts from multiple listings
all_posts = list(subreddit.hot(limit=500)) + \
            list(subreddit.new(limit=500)) + \
            list(subreddit.top("all", limit=500))

# Remove duplicates
unique_posts = {post.id: post for post in all_posts}.values()

posts = []
for i, submission in enumerate(unique_posts, start=1):
    print(f"Processing post {i}...", end="\r")  # live progress

    # Skip posts with images/videos/links
    if getattr(submission, "post_hint", None) in ["image", "video", "link"]:
        continue

    # Skip posts with empty selftext
    if not submission.selftext.strip():
        continue

    # Detect Slovenian
    try:
        if detect(submission.title + " " + submission.selftext) != "sl":
            continue
    except:
        continue  # skip if language detection fails
    
    # Collect post data
    posts.append({
        "title": submission.title,
        "score": submission.score,
        "id": submission.id,
        "url": submission.url,
        "num_comments": submission.num_comments,
        "created_utc": submission.created_utc,
        "selftext": submission.selftext
    })

# Create DataFrame
df = pd.DataFrame(posts)

# Save CSV with timestamp on Desktop
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
csv_path = os.path.join(desktop, f"{subreddit_name}_slovenian_posts_{timestamp}.csv")
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

print(f"✅ Saved {len(df)} Slovenian text-only posts to CSV at {csv_path}")