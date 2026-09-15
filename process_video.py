import os
import subprocess

files = os.listdir("RAG PROJECT/videos")

for file in files:
    tutorial_name = file.split("_")[1].split(".")[0]
    tutorial_number = file.split("_")[0]
    print(tutorial_number,tutorial_name)

    subprocess.run(["ffmpeg", "-i", f"RAG PROJECT/videos/{file}", f"RAG PROJECT/audios/{tutorial_number}_{tutorial_name}.mp3"])
