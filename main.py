import requests
from bs4 import BeautifulSoup

def scout_web(url):
    print(f"[*] Scouting data from: {url}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            print(f"[+] Successfully scraped! Page Title: {title}")
        else:
            print(f"[-] Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    # Example target URL
    target_url = "https://example.com"
    scout_web(target_url)
