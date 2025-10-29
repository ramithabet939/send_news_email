import requests
from send_email import send_email
topic = "tesla"
url = 'https://newsapi.org/v2/everything?q=tesla&from=2025-09-29&sortBy=publishedAt&apiKey=26c3dd6a5c3a43ef8e453e903b94e701&language=en'
response = requests.get(url)
api_key = '26c3dd6a5c3a43ef8e453e903b94e701'

#MAKE REQUEST
request = requests.get(url)

#get a dictionary with data
content = request.json()

# Access the article title and description
body = ''
for article in content['articles'][0:20]:
    body = "Subject: Today's News"+ '\n' +body + article['title'] + '\n' + article['description'] + '/n'+ article['url']+2*'\n'

body = body.encode('utf-8')
send_email(message=body)
