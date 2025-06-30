import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

def get_spotify_client():
    SPOTIPY_CLIENT_ID= os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET= os.getenv("SPOTIPY_CLIENT_SECRET")

    if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
        raise Exception("Spotify credentials not found")
    
    auth_manager = SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)
