# 🚀 How to Run the Project (Step-by-Step Guide)

This guide explains how to execute the **RAG-Based AI Teaching Assistant** from start to finish.

---

## 📁 Step 1: Collect Videos

Download **20+ educational videos** from the internet (any topic is fine).

### 📌 Important Naming Convention

Make sure all videos follow a **consistent naming format**, for example:

```
Installing VS Code & How Websites Work _ Sigma Web Development Course - Tutorial _1(720P_HD)
Introduction to CSS _ Sigma Web Development Course - Tutorial _2(720P_HD)
Video, Audio & Media in HTML _ Sigma Web Development Course - Tutorial _3(720P_HD)
```

✅ Proper naming ensures smooth processing and correct ordering during transcription.

Place all video files inside the designated **videos/** directory.

---

## 🎵 Step 2: Convert Video to MP3

Run the script below to extract audio from all videos:

```
python video_to_mp3.py
```

📌 This step uses **FFmpeg + Python subprocess** to convert videos into MP3 format.

Output will be saved in the **audios/** directory.

---

## 📝 Step 3: Convert MP3 to JSON (Speech-to-Text)

Convert audio files into text transcripts using Whisper:

```
python mp3_to_json.py
```

📌 Uses **Whisper (large-v2)** to generate structured JSON transcripts.

Output will be saved in the **jsons/** directory.

---

## 🧩 Step 4: Merge Transcript Chunks

Improve context by merging multiple short transcript lines into meaningful chunks:

```
python merge_chunks.py
```

📌 This script merges **5 single-line chunks into one semantic chunk** for better retrieval quality.

Output will be saved as **new_jsons/** directory.

---

## ⚙️ Step 5: Preprocess JSON Files

Prepare transcript data and user queries for embedding generation:

```
python preprocess_json.py
```

📌 This step cleans, formats, and prepares data for vector embedding.

---

## 🤖 Step 6: Process User Query & Generate Response

Finally, run the main pipeline to retrieve relevant context and generate an answer:

```
python process_incoming.py
```

📌 This step:

* Converts user input into embeddings
* Retrieves relevant chunks
* Generates a response using the LLM (LLaMA 3.2)

---

## ✅ Execution Flow Summary

```
Videos
  ↓
video_to_mp3.py
  ↓
mp3_to_json.py
  ↓
merge_chunks.py
  ↓
preprocess_json.py
  ↓
process_incoming.py
```

---

## ⚠️ Notes

* Ensure **FFmpeg** is installed and added to PATH
* Recommended RAM: **8 GB minimum**
* LLaMA 3.2 is used by default
* Pipeline supports **GPT-5**, but higher system memory is required

---

## ⚠️ Processing Time & System Load Disclaimer

The **video-to-audio** and **audio-to-text** steps are **computationally expensive** and may take a significant amount of time depending on your system configuration.

### ⏱️ Expected Processing Time

* Total videos processed: **18**
* Average time per file (MP3 → JSON using Whisper large-v2): **~1 hour per file**
* Total transcription time can exceed **18+ hours** on CPU-only systems

### 🧠 System Limitations

* This project was executed on a system with **8 GB RAM**
* Running transcription on **multiple files simultaneously may overload your system**
* High CPU and memory usage is expected during execution

### 🔄 Execution Strategy Used

* Code supports **processing MP3 files sequentially (one-by-one)** to reduce system load
* For systems with limited RAM or no GPU:

  * It is **strongly recommended** to process files **individually**
  * Execute the transcription script for **one file at a time**

### 🛠️ Practical Approach Followed

* Transcription was performed **separately for each MP3 file**
* After processing one file:

  * The filename was updated manually
  * The script was re-run for the next file
* This approach ensures **stability** on low-memory systems

### 📌 Recommendation

If your system cannot handle batch processing:

* Modify the script to accept **a single filename**
* Process files **one at a time**
* Avoid parallel execution unless sufficient RAM and GPU resources are available

---

## 📌 Final Tip

Follow the steps **in the same order** for correct execution.

---

