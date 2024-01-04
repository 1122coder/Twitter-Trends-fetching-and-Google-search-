import requests
from bs4 import BeautifulSoup

def fetch_twitter_trends(url):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data based on the structure of the webpage
        trends = soup.find_all('li', {'class': 'list-group-item'})  # Finding list items for each trend

        trend_data = []
        for trend in trends:
            trend_name = trend.find('a').get_text(strip=True)  # Get the text within the anchor tag for the trend name
            trend_volume = trend.find('span').get_text(strip=True)  # Get the volume of tweets
            trend_data.append((trend_name, trend_volume))
        print('Fetching trends')
        return trend_data

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

# URL of the page to scrape
url = 'https://w3trends.net/pakistan'

# Fetch and print Twitter trends
trends = fetch_twitter_trends(url)
for title, volume in trends:
    print(f"Trend: {title}, Volume: {volume}")
