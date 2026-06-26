
import numpy as np
import pandas as pd # type: ignore
import os
import lyricsgenius
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# TODO: handle None returns from genius.search_song and search_album


genius = lyricsgenius.Genius("YOUR_GENIUS_TOKEN_HERE")
artist_albums = {}

def search_artist_album(artist_name, album_name, word_search):
    dict = {}  
    album = genius.search_album(artist_name, album_name)
    if album is None:
        print(f"{album_name} doesn't exist")
        return 0
    for track_number, song in album.tracks:
        count = song.lyrics.lower().count(word_search.lower())
            
        # song_list.append(count)
        dict[song.title] = count
    artist_albums[album_name] = dict
    
    return dict



def search_artist_song(artist_name, song_name, word_search):
    song = genius.search_song(song_name, artist_name)
    try:
        if song is None:
            raise ValueError(f"{song_name} doesnt exsit")
    except ValueError as e:
        print(e)
        return -1

    count = song.lyrics.lower().count(word_search.lower())
    return count

    # Search for the artist and album
    
def creating_dataframe(artist_albums):
    data = []
    for album_name, songs in artist_albums.items():
        for song_title, count in songs.items():
            data.append({'Album': album_name, 'Song': song_title, 'Count': count})
    
    df = pd.DataFrame(data)
    df['Has Word'] = df['Count'] > 0
    
    return df


def main():
    Album_save = {}
    song_save = {}
    while True:
        
        input_option = input("would you like to search  for a song or artist? (y/n): ")
        try:
            if input_option not in ["y", "n"]:
                raise ValueError("Invalid input. Please enter 'y' or 'n', stop acting like a ozwor and enter the right input.")
        except ValueError as e:
            print(e)
            continue


        if input_option == "n":
            break

        
        input_option = input("Would you like to search for a song or Album : ")
        try:
            if input_option not in ["Album", "song"]:
                raise ValueError("Invalid input. Please enter 'Album' or 'song', stop acting like a ozwor and enter the right input.")
        except ValueError as e:
            print(e)
            continue

        
        if input_option == "Album":
            
            input_artist = input("Enter the artist's name: ")
            input_album = input("Enter the album's name: ")
            word_search = input("Enter the word to search for in the lyrics: ")
            artist_ser = genius.search_artist(input_artist,max_songs = 0)
            if artist_ser is not None:
                dict = search_artist_album(input_artist, input_album, word_search)
                if dict == 0: # if it album doesnt exsit
                    continue
                Album_save[input_album] = dict
               
            else:
                 print(f"{input_artist} is not found")
                 os.system('cls' if os.name =='nt' else 'clear')
                 continue
            os.system('cls' if os.name =='nt' else 'clear') # to clear the screen

        elif input_option == "song":
            input_artist = input("Enter the artist's name: ")
            input_song = input("Enter the song's name: ")
            word_search = input("Enter the word to search for in the lyrics: ")
            artist_serh = genius.search_artist(input_artist,max_songs = 1)
            if artist_serh is not None:
                count = search_artist_song(input_artist, input_song, word_search)
                if count == -1:
                    continue
                song_save[input_song] = count
            else:
                print(f"{input_artist} is not found")
                os.system('cls' if os.name =='nt' else 'clear')
                continue
            os.system('cls' if os.name =='nt' else 'clear')
    
      
    print("Album search results:")
    for album_name, song_counts in Album_save.items():
        print(f"Album: {album_name}")
        for song_title, count in song_counts.items():
            print(f"  Song: {song_title}, Count: {count}")

    print("\nSong search results:")
    for song_name, count in song_save.items():
        print(f"  Song: {song_name}, Count: {count}")


    
    os.system('cls' if os.name =='nt' else 'clear')
    result = input("would you like to see the data and graph (y/n): ")
    try:
        if result not in ["y","n"]:
            raise ValueError("Invalid input. Please enter 'y' or 'n', stop acting like a ozwor and enter the right input.")
    except ValueError as e:
        print(e)

    if result == "y":
        df = creating_dataframe(Album_save)
        print(df)
        album_totals = df.groupby('Album')['Count'].sum()
        album_totals.plot(kind='bar', color='black', edgecolor='white')
        plt.title('Total "ikebe" mentions per album')
        plt.xlabel('Album')
        plt.ylabel('Total Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        
    else:
        print("bye bye")

if __name__ == "__main__":
    main()