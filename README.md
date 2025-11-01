# Reddit Scraper for Slovenian Posts (/r/Ljubljana)

This repository contains a Python script for **automatically collecting Slovenian-language posts** from the [r/Ljubljana](https://www.reddit.com/r/Ljubljana) subreddit using the Reddit API. The scraper retrieves textual posts, filters out non-text and non-Slovenian content, and exports the results as a structured CSV file — suitable for **corpus linguistics**, **sociolinguistic analysis**, or **NLP research** involving informal Slovene online discourse.

---

## 🧩 Features

- Retrieves posts from Hot, New, and Top (All-Time) categories  
- Detects and retains only Slovenian-language posts (`langdetect`)  
- Excludes images, videos, and links  
- Saves a UTF-8 encoded CSV (compatible with Excel and corpus tools)  
- Automatically timestamps each export  
- Ensures unique post IDs (no duplicates)

---

## 📁 Output Example

Each row in the CSV file corresponds to one Reddit post:

| id | title | selftext | score | url | num_comments | created_utc |
|----|--------|-----------|--------|----------------|--------------|
| t3_xabcd | Ljubljanski promet | Danes spet zastoji na Celovški. | 52 | https://redd.it/xabcd | 13 | 1730462100 |

**Example filename:**  Ljubljana_slovenian_posts_20251101_123806.csv

---

## 🚀 Usage

Run the scraper from the command line: python reddit_scraper.py

The script:
- Connects to Reddit through PRAW
- Collects up to 1500 posts (500 from each category)
- Filters out non-Slovenian or media-based content
- Saves the resulting dataset as a timestamped CSV on your Desktop
- Terminal output shows live progress and the final count of saved posts

---

## 🧾 Example Use Cases

- Building a corpus of Slovene online discourse
- Studying urban discourse or sociolinguistic patterns in online communities
- Training or testing NLP models on informal Slovene text
- Performing sentiment or topic analysis on local Reddit discussions

---

## 🧹 Cleanup and Performance

- Execution typically takes 1–3 minutes, depending on API response speed.
- The script automatically handles language detection errors and skips problematic posts.
- Reddit connections close automatically after data retrieval.
