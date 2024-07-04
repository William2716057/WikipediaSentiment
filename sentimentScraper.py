import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# URL to scrape
url = input("Enter Wikipedia article URL : ")

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the content between <title></title> 
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text()
        print(f'Title Tag Content: {title}')
    
    # Extract content in <h1> tags
    h1_tag = soup.find('h1', id='firstHeading')
    if h1_tag:
        h1_title = h1_tag.get_text()
        print(f'Article Title: {h1_title}')
    
    # Extract article content from relevant tags
    article_content = ''
    content_div = soup.find('div', id='mw-content-text')
    if content_div:
        paragraphs = content_div.find_all('p')
        for paragraph in paragraphs:
            article_content += paragraph.get_text() + '\n'
    
    print(f'Article Content: {article_content}')
else:
    print(f'Failed. Status code: {response.status_code}')
    
blob = TextBlob(article_content)

sentiment = blob.sentiment
print("Sentiment of Article: ", sentiment)