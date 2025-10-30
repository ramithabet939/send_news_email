## 📰 Send News Email

A simple Python automation script that fetches the latest news articles on a specific topic (like **Tesla**) using the [NewsAPI](https://newsapi.org/) and sends them straight to your email inbox.

---

##  Features
- Fetches live news articles from NewsAPI  
- Sends a summarized email with titles, descriptions, and links  
- Supports language and sorting options  
- Easy to customize topic, article limit, and date range  

---

##  How It Works
1. Uses the `requests` library to fetch JSON data from the NewsAPI.  
2. Extracts each article’s **title**, **description**, and **URL**.  
3. Builds a readable email body.  
4. Sends the email using the custom `send_email()` function from `send_email.py`.



---

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ramithabet939/send_news_email.git
   cd send_news_email


pip install requests

## Example Output
Subject: Today's News

Tesla shares rise after record earnings
Tesla announced record profits in Q3...
https://example.com/article1

Elon Musk unveils new Gigafactory
The new facility will boost battery production...
https://example.com/article2

## Tech Stack
Language: Python

Libraries: requests, smtplib

API: NewsAPI
