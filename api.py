from flask import Flask, json
from youtube.youtubeFetcher import YoutubeFetcher

app = Flask(__name__)

youtubeFetcher = YoutubeFetcher()


@app.route("/youtube/<q>")
def get_youtube_videos(q):
    data = youtubeFetcher.youtube_search(q, 25)
    return app.response_class(response=json.dumps(data),
                              status=200,
                              content_type="application/json")


if __name__ == "__main__":
    app.run()
