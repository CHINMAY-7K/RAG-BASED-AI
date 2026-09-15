import whisper
import os
import json
import torch

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

model = whisper.load_model("large-v2", device=device)

# Relative path from where your terminal is running
audios_dir = os.path.join("RAG PROJECT", "audios")
audios = os.listdir(audios_dir)

for audio in audios:
    # Build exact full system path automatically
    audio_path = os.path.abspath(os.path.join(audios_dir, audio))

    number = audio.split("_")[0]
    title = audio.split("_")[1].split(".")[0]
    print(number, title)

    result = model.transcribe(
        audio=audio_path,
        language="hi",
        task="translate",
        word_timestamps=False,
        fp16=(device == "cuda")
    )

    chunks = []

    for segment in result["segments"]:
        chunks.append({
                "number":number,
                "title":title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
                })

    Chunks_with_metadata = {
            "chunks": chunks,
            "text": result["text"]

            }
 

    with open(f"RAG PROJECT/jsons/{audio}.json", "w", encoding="utf-8") as f:
        json.dump(Chunks_with_metadata, f, ensure_ascii=False, indent=2)