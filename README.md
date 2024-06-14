## 🎼Billboard and Spotify Hot Song Recommender🎵:


The goal is to create a song recommendation system using a machine learning clustering approach. This system involves three main functions: `scrape_billboard()`, ``audio()``, and ``spoti()``, culminating in the final function hot_recommender().

1. Scrape Billboard Data: ``scrape_billboard()``
The scrape_billboard() function scrapes the Billboard website for the current top 100 chart and creates a DataFrame with the top 100 songs and their respective artists. This DataFrame is refreshed every time the code runs, ensuring up-to-date chart data that will be used later in the recommendation process.

2. Retrieve Audio Features: ``audio()``
The audio() function retrieves Spotify API credentials (client ID and token) from environment variables and authenticates using the SpotifyClientCredentials manager from the spotipy library. The function prompts the user to input an artist's name and searches for up to 50 tracks by the specified artist on Spotify. It extracts track IDs and names, retrieves their audio features using the audio_features method, and organizes this data into a Pandas DataFrame. This DataFrame includes various audio metrics such as tempo, key, and loudness, which will be used for further analysis and song recommendations.

3. Song Recommendation: ``spoti()``
The spoti() function leverages the audio() function to get a DataFrame of audio features for up to 50 songs by a user-specified artist. It selects specific audio features, standardizes them using StandardScaler, and applies K-Means clustering to group the songs into clusters. The function creates a new DataFrame with the standardized features, song names, artist names, and assigned clusters.

When the user inputs a song name for recommendation, spoti() searches for the specified song on Spotify, retrieves its track ID and audio features, and confirms the song with the user. If confirmed, it standardizes the song's audio features, predicts its cluster, and filters the DataFrame to include only songs in the same cluster. The function then identifies the closest song in this cluster to the specified song using the pairwise_distances_argmin_min function, prints the recommended song's name and artist, and opens the recommended song in the user's web browser.

4. Final Recommendation: ``hot_recommender()``
The hot_recommender() function integrates all the components to provide a comprehensive song recommendation system. It imports the spoti() function, the scrape_billboard() function, and the randint function.

The hot_recommender() function performs the following steps:

Scrapes the current Billboard chart data using scrape_billboard().
Prompts the user to input a song name they like.
Checks if the song is on the Billboard list. If found, it confirms the song with the user and suggests another song from the Billboard list. If the song is not found, it uses the spoti() function to recommend a similar song based on audio features from the Spotify API.

So in summary:

The system provides personalized song recommendations by combining real-time Billboard chart data with audio feature analysis and machine learning clustering. The spoti() function is at the core, utilizing Spotify's audio features and clustering to find and recommend songs with similar characteristics. The hot_recommender() function adds an extra layer by integrating Billboard popularity checks, ensuring users get both hot chart recommendations and personalized suggestions.

