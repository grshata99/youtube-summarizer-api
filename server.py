from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.json
    url = data.get("youtubeUrl")
    if not url:
        return jsonify({"error": "Missing YouTube URL"}), 400

    try:
        video_id = url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item["text"] for item in transcript])
        return jsonify({
            "summary": f"This is a placeholder summary. Transcript length: {len(full_text)} characters."
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
