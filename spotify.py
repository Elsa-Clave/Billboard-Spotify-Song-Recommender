def spoti(song_name):
    from artistas import audio

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


    #song_name = input('Choose a song: ')
    df=audio()
 

    x = df[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]

    # standarize the data
    scaler = StandardScaler()
    x_prep = scaler.fit_transform(x)
    kmeans = KMeans(n_clusters=9, random_state=42)
    kmeans.fit(x_prep)
    clusters = kmeans.predict(x_prep)

    #create new dataframe with title, artist and cluster assigned
    scaled_df = pd.DataFrame(x_prep, columns=x.columns)
    scaled_df['song_name'] = df["song_name"]
    scaled_df['artist'] = df['artist']
    scaled_df['cluster'] = clusters

        #SONG RECOMMENDATON
    
    # get song id
    
    results = sp.search(q=f'track:{song_name}', limit=1)

    print(f'You choosed {results["tracks"]["items"][0]["name"]} by {results["tracks"]["items"][0]["artists"][0]["name"]}')
    track_id = results['tracks']['items'][0]['id']

    right=input(f'Is {results["tracks"]["items"][0]["name"]} by {results["tracks"]["items"][0]["artists"][0]["name"]} your song?')
    if right.lower() not in ["yes", "y", "si", "affirmative"]:
        print("We could not find your song")
        return 
    # get song features with the obtained id
    audio_features = sp.audio_features(track_id)
    
    # create dataframe
    df_ = pd.DataFrame(audio_features)
    new_features = df_[x.columns]
    
    # scale features
    scaled_x = scaler.transform(new_features)
    
    # predict cluster
    cluster = kmeans.predict(scaled_x)
    
    # filter dataset to predicted cluster
    filtered_df = scaled_df[scaled_df['cluster'] == cluster[0]][x.columns]
    
    # get closest song from filtered dataset
    closest, _ = pairwise_distances_argmin_min(scaled_x, filtered_df)
    
    # return it in a readable way
    print(f'You choosed {results["tracks"]["items"][0]["name"]} by {results["tracks"]["items"][0]["artists"][0]["name"]}')
    print('\n [RECOMMENDED SONG]')
    print(' - '.join([scaled_df.loc[closest]['song_name'].values[0], scaled_df.loc[closest]['artist'].values[0]]))

    nuevo=' - '.join([scaled_df.loc[closest]['song_name'].values[0], scaled_df.loc[closest]['artist'].values[0]])
    import webbrowser
    import time
    time.sleep(5)
    opensong=sp.search(q=nuevo, limit=1)
    browser=opensong["tracks"]["items"][0]["external_urls"]["spotify"]
    webbrowser.open(browser)

