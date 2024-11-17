# 5) Extract any website data using Beautiful Soup.

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_3oes7cd2fz_e&adgrpid=1324913168722107&hvadid=82807336663554&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=157506&hvtargid=kwd-82808007665574:loc-90&hydadcr=5620_2377278&msclkid=4013ee04e4af1a9bc5eb89241cc45ca1'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all article titles (assuming they are in <h2> tags)
titles = soup.find_all('h2')

# Print the titles
for title in titles:
    print(title.get_text())