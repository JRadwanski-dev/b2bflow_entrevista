import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


manchetes = soup.find_all('a', class_='feed-post-link', limit=10)
titulos = [manchete.get_text(strip=True) for manchete in manchetes]


with open("manchetes_g1.txt", "w", encoding="utf-8") as f:
    f.write("Manchetes principais do G1:\n\n")
    for titulo in titulos:
        f.write(f"- {titulo}\n")





