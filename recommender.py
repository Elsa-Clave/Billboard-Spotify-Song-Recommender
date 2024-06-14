def hot_recommender():
    from spotify import spoti
    from billboard_scraper import scrape_billboard
    from random import randint

    billboard=scrape_billboard()
    song=input("What song do you like?")

    song_row=billboard[billboard["song"].str.contains(song)]
    if len(song_row)==0:
        print("YOUR SONG IS NOT HOT!")
        spoti(song)
    
    else:
        check_song=input("Did you mean " + song_row["song"].values[0]+ " by " + song_row["artist"].values[0]+ "?")
        if check_song.lower() in ["yes", "y", "confirmed", "si"]:
            print("That's a HOT SONG")
            random_song=randint(0, len(billboard)-1)
            print(f"You will also like {billboard['song'][random_song]} by {billboard['artist'][random_song]}")
        else:
            print("Ah, not the one that I had in mind.")

         
         