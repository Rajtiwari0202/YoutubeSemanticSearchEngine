from youtube_transcript_api import YouTubeTranscriptApi
import json
import os

VIDEO_ID = "kqtD5dpn9C8"

api = YouTubeTranscriptApi()

transcript = api.fetch(VIDEO_ID)

os.makedirs("data/transcripts", exist_ok=True)

data = []

for item in transcript:
    data.append({
        "text": item.text,
        "start": item.start,
        "duration": item.duration
    })

with open(
    f"data/transcripts/{VIDEO_ID}.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(data)} transcript segments")