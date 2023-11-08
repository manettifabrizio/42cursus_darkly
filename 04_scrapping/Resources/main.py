import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_directory(url):
    visited = set()
    to_visit = [url]

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue

        visited.add(current_url)
        response = requests.get(current_url)
        if response.status_code != 200:
            print(f"Failed to retrieve {current_url}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href != "../":
                new_url = urljoin(current_url, href)
                to_visit.append(new_url)
                if href.endswith("README"):
                    readme_content = requests.get(new_url).text
                    disallowed_phrases = [
                        "Tu veux de l'aide ? Moi aussi !",
                        "Demande à ton voisin du dessous",
                        "Demande à ton voisin du dessus",
                        "Demande à ton voisin de gauche",
                        "Demande à ton voisin de droite",
                        "Toujours pas tu vas craquer non ?",
                        "Non ce n'est toujours pas bon ..."
                    ]
                    if any(phrase in readme_content for phrase in disallowed_phrases):
                        break
                    else:
                        print(new_url)
                        print(readme_content)


url = "http://192.168.64.13/.hidden/"
scrape_directory(url)
