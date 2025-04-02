import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic
import json

# Load configurations from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

SPOTIPY_CLIENT_ID = config["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = config["SPOTIPY_CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))

# YouTube Music Authentication
yt = YTMusic("oauth.json")  # Ensure you have authenticated using YTMusic API

def get_spotify_playlist_tracks(playlist_id):
    """ Fetch all track names and artists from a public Spotify playlist."""
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for item in results['items']:
        track = item['track']
        if track:  # Ensure track exists
            name = track['name']
            artist = track['artists'][0]['name']
            tracks.append(f"{name} {artist}")
    return tracks

def search_youtube_music(track_name):
    """ Search for a track on YouTube Music."""
    search_results = yt.search(track_name, filter="songs")
    if search_results:
        return search_results[0]['videoId']  # Get first result's video ID
    return None

def create_youtube_music_playlist(name, description, tracks):
    """ Create a YouTube Music playlist and add tracks."""
    playlist_id = yt.create_playlist(name, description)
    video_ids = [search_youtube_music(track) for track in tracks]
    video_ids = [vid for vid in video_ids if vid]  # Remove None values
    yt.add_playlist_items(playlist_id, video_ids)
    return playlist_id

def convert_spotify_to_youtube(spotify_playlist_id, yt_playlist_name, yt_playlist_desc):
    """ Convert a public Spotify playlist to YouTube Music."""
    print("Fetching Spotify playlist tracks...")
    tracks = get_spotify_playlist_tracks(spotify_playlist_id)
    if not tracks:
        print("No tracks found or playlist is private.")
        return
    print("Creating YouTube Music playlist...")
    playlist_id = create_youtube_music_playlist(yt_playlist_name, yt_playlist_desc, tracks)
    playlist_url = f"https://music.youtube.com/playlist?list={playlist_id}"
    print(f"Playlist created: {playlist_url}")
    return playlist_url

# Example usage
SPOTIFY_PLAYLIST_ID = "your_spotify_playlist_id"
youtube_playlist_url = convert_spotify_to_youtube(SPOTIFY_PLAYLIST_ID, "Converted from Spotify", "Auto-generated from Spotify playlist")