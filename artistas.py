def audio():
    from dotenv import load_dotenv
    import os
    import warnings
    warnings.filterwarnings("ignore")

    import spotipy
    import pandas as pd
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    from spotipy.oauth2 import SpotifyClientCredentials
    from sklearn.metrics import pairwise_distances_argmin_min

    load_dotenv()
    user=os.getenv("client")
    password=os.getenv("token")

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=user, client_secret=password))

    artist=input("Please select an artist to recommend one of his songs based on your song:")
    results=sp.search(q=f'artist:{artist}', limit=50)

    track_ids=[track["id"] for track in results["tracks"]["items"]]
    song_names=[track["name"] for track in results["tracks"]["items"]]

    audio_features=sp.audio_features(track_ids)
    df=pd.DataFrame(audio_features)
    df["artist"]=artist
    df["song_name"]=song_names
    return df