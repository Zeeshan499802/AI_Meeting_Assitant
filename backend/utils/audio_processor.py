import yt_dlp
from pydub import AudioSegment
import os

# =========================
# CONFIG
# =========================

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

FFMPEG_BIN = r"C:\Users\DELL\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

# Ensure ffmpeg is in PATH
os.environ["PATH"] += os.pathsep + FFMPEG_BIN


# =========================
# YOUTUBE DOWNLOAD
# =========================

def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "ffmpeg_location": FFMPEG_BIN,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        final_path = os.path.join(DOWNLOAD_DIR, f"{info['id']}.mp3")

        if not os.path.exists(final_path):
            raise Exception(f"MP3 conversion failed: {final_path}")

        return final_path


# =========================
# CONVERT ANY AUDIO → WAV
# =========================

def convert_to_wav(input_file: str) -> str:
    if not os.path.exists(input_file):
        raise FileNotFoundError(input_file)

    output_path = os.path.splitext(input_file)[0] + "_converted.wav"

    # FIX: auto detect format (mp3/webm/m4a/wav)
    audio = AudioSegment.from_file(input_file)

    audio = audio.set_channels(1).set_frame_rate(16000)

    audio.export(output_path, format="wav")

    return output_path


# =========================
# CHUNK AUDIO (SAFE)
# =========================

def chunk_audio(audio_path: str, chunk_minutes: int = 10) -> list:
    # FIX: auto format detection (IMPORTANT FIX)
    audio = AudioSegment.from_file(audio_path)

    chunk_length_ms = chunk_minutes * 60 * 1000
    chunks = []

    for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
        chunk = audio[start:start + chunk_length_ms]

        chunk_path = f"{audio_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")

        chunks.append(chunk_path)

    return chunks


# =========================
# MAIN PIPELINE
# =========================

def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print(f"Downloading audio from YouTube: {source}")
        audio_path = download_youtube_audio(source)
    else:
        print("Detected local file. Converting to WAV...")
        audio_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(audio_path)

    print(f"Audio ready - {len(chunks)} chunks created.")
    return chunks