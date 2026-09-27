import json
import os

VIDEO_ID = "kqtD5dpn9C8"

INPUT_FILE = f"data/transcripts/{VIDEO_ID}.json"
OUTPUT_FILE = f"data/chunks/{VIDEO_ID}_chunks.json"

os.makedirs("data/chunks", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    transcript = json.load(f)

chunks = []

current_text = []
chunk_start = None

WORD_LIMIT = 200

for segment in transcript:

    if chunk_start is None:
        chunk_start = segment["start"]

    current_text.append(segment["text"])

    words = " ".join(current_text).split()

    if len(words) >= WORD_LIMIT:

        chunk_end = (
            segment["start"]
            + segment["duration"]
        )

        chunks.append(
            {
                "text": " ".join(current_text),
                "start": chunk_start,
                "end": chunk_end
            }
        )

        current_text = []
        chunk_start = None

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:
    json.dump(chunks, f, indent=2)

print(f"Created {len(chunks)} chunks")