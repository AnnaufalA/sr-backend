import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

SPOTIPY_CLIENT_ID = "bdc294278dba454abccbb05182e18d95"  
SPOTIPY_CLIENT_SECRET = "5d9987b0d220439992eb15c2da72a712"

def get_spotify_client():
    print("Spotify ID:", SPOTIPY_CLIENT_ID)
    print("Spotify Secret:", SPOTIPY_CLIENT_SECRET)

    if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
        raise Exception("Spotify credentials not found")
    
    auth_manager = SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)
