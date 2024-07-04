# Wikipedia Article Scraper and Sentiment Analysis

This repository contains a Python script that scrapes the content of a specified Wikipedia article and performs sentiment analysis on the article's text using TextBlob.

## Installation
First, ensure you have Python installed on your machine. Then, install the required libraries.

`
pip install requests
`

`
pip install beautifulsoup4
`

`
pip install textblob
`

## Usage
This script prompts the user to enter a Wikipedia article URL, scrapes the content of the article, and performs sentiment analysis on the text.

## Explanation
1. Import Libraries: The script imports requests for making HTTP requests, BeautifulSoup from bs4 for parsing HTML, and TextBlob for performing sentiment analysis.

2. URL Input: The script prompts the user to enter a Wikipedia article URL.

3. Sending GET Request: The script sends a GET request to the specified URL and checks if the request was successful.

4. Parsing HTML Content: If the request is successful, the script parses the HTML content using BeautifulSoup.

5. Extracting Title Tag Content: The script finds and prints the text content within the <title> tag.

6. Extracting H1 Tag Content: The script finds and prints the text content within the first h1 tag with the id of firstHeading.

7. Extracting Article Content: The script finds the div with the id of mw-content-text, then extracts and concatenates the text content of all p tags within that div. The combined content is then printed.

8. Performing Sentiment Analysis: The script creates a TextBlob object with the extracted article content and prints the sentiment of the article.
