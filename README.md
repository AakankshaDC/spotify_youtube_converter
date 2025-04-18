# README
## Generate Spotify API Creds
1. Go to https://developer.spotify.com/dashboard
2. Create App
3. Click on your profile and find client id and secret under Basic Information
4. Create a file called `config.json` in your local repo that should look like -
```
{
    "SPOTIPY_CLIENT_ID": "your_spotify_client_id",
    "SPOTIPY_CLIENT_SECRET": "your_spotify_client_secret"
}
```
5. Paste values from the dashboard in the file

## Generate YT Music Creds
When running ytmusicapi oauth, it asks for Google YouTube Data API credentials. Here’s how to get the required Client ID and Secret:

### Steps to Get Google YouTube Data API Client ID & Secret
1. Go to Google Cloud Console - https://console.cloud.google.com/ 
2. Create a New Project (or select an existing one).
3. Enable the YouTube Data API v3:
    a. Go to APIs & Services > Library.
    b. Search for YouTube Data API v3 and enable it.
4. Create OAuth 2.0 Credentials:
    a. Go to APIs & Services > Credentials.
    b. Click "Create Credentials" → OAuth client ID.
    c. Select "Desktop App" as the Application Type.
    d. Click "Create" and note down the Client ID and Client Secret.
5. Use These Values in ytmusicapi oauth:
    a. When ytmusicapi oauth asks for Google YouTube Data API Client ID and Secret, enter the values from step 4.

Once done, it will generate oauth.json, which is needed for authenticating YouTube Music API requests.

## Install Dependencies 
Run `pip3 install flask spotipy ytmusicapi`

## Running the App
```
python app.py
```
Visit http://127.0.0.1:5000/ in your browser, enter a Spotify playlist URL, and click Submit.
