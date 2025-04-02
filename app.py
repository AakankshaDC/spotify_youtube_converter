from flask import Flask, render_template, request
from spotify_youtube_converter import convert_spotify_to_youtube

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    youtube_playlist_url = None
    if request.method == "POST":
        spotify_url = request.form.get("spotify_url")
        if spotify_url:
            youtube_playlist_url = convert_spotify_to_youtube(spotify_url, "Converted from Spotify", "Auto-generated playlist")
    return render_template("index.html", youtube_playlist_url=youtube_playlist_url)

if __name__ == "__main__":
    app.run(debug=True)
