# How to use this RAG AI Teaching assistant on your own data

## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning ##process_video

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning ##create_chunks

## Step 4 - Convert the json files to Vectors
Use the file ##read_chunks to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM




## Features
- Video-to-text processing
- Text chunking
- Embedding generation
- Semantic retrieval
- LLM-based response generation

  

## Architecture
Video
 ↓
Audio Extraction
 ↓
Speech-to-Text
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Retrieval
 ↓
Relevant Context
 ↓
LLM
 ↓
Answer


## Tech Stack
Python |
RAG |
NLP |
Embeddings |
LLM |
Git/GitHub 

