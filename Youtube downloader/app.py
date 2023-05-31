from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("HomePage.html")

@app.route("/download", methods=["POST"])
def downloadPage():
    YouTubeLink = request.form.get('YoutubeLink')
    try:
        yt = YouTube(YouTubeLink)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download()
        
        filename = os.path.basename(file_path)
        return send_file(file_path, as_attachment=True, attachment_filename=filename)
    except Exception as e:
        return f"<h1>{e}</h1>"

if __name__ == '__main__':
    app.run()
