from bs4 import BeautifulSoup

# Load your HTML content
with open('facebook_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
#zzzz
# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags and extract href attributes
links = [a.get('href') for a in soup.find_all('a')]

# Print the href attributes
with open('links.txt', 'w', encoding='utf-8') as file:
    for link in links:
        file.write(f"https://www.facebook.com{link}\n")