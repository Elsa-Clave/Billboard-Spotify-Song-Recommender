# billboard_scraper.py
def scrape_billboard():

    from bs4 import BeautifulSoup
    import requests 
    import pandas as pd

    url = "https://www.billboard.com/charts/hot-100/"
    headers = {"User-Agent": "MiAplicacion/1.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud HTTP: {e}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    
    clean_songs = []
    songs = soup.find_all('h3', class_='a-no-trucate')
    for h3_tag in songs:
        clean = h3_tag.get_text(strip=True)
        clean_songs.append(clean)
    
    clean_artists = []
    artists = soup.find_all('span', class_='a-no-trucate')
    for span_tag in artists:
        clean2 = span_tag.get_text(strip=True)
        clean_artists.append(clean2)
    
    billboard = pd.DataFrame({'song': clean_songs, 'artist': clean_artists})
    return billboard
