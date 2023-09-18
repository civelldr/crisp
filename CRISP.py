# civelldr revolutionary interface for song playlists...CRISP!
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os 

# get API keys from spotify developer dashboard
# stick the values in your .zshrc or .bashrc as environment variables, i.e.
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
# and don't forget to source your .zshrc or .bashrc after you add them
#
# pro-tip, use http://localhost:8080/callback as redirect uri, first time
# you run this script, it will open a browser window and ask you to login


SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

playlist_name = "Darkwave Selection"
artists = [
    "She Past Away",
    "Lebanon Hanover",
    "Drab Majesty",
    "Cold Cave",
    "Boy Harsher",
    "Ash Code",
    "The Soft Moon",
    "Linea Aspera",
    "Actors",
    "Hante.",
    "Selofan",
    "Twin Tribes",
    "Kaelan Mikla",
    "Light Asylum",
    "Sixth June"
]

# Initialize Spotipy with user auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-library-read user-top-read playlist-modify-private playlist-modify-public"
))

# get artist's top tracks
def get_artist_top_tracks(artist_name):
    results = sp.search(q=f"artist:{artist_name}", type="artist")
    artist_id = results["artists"]["items"][0]["id"]
    top_tracks = sp.artist_top_tracks(artist_id)
    return [track["id"] for track in top_tracks["tracks"]]

# Create playlist and add tracks
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
playlist_id = playlist["id"]


track_uris = []

for artist in artists:
    top_tracks_uris = get_artist_top_tracks(artist)
    track_uris.extend(top_tracks_uris[:5])  # limit to top 5

# you should have a playlist with 75 tracks now. I don't know if they are good or not, but they are there!
sp.playlist_add_items(playlist_id, track_uris)