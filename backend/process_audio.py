import librosa
import numpy as np

audio_file_path = "path/to/your/local/audio.mp3"

librosa.load(audio_file_path)
sr = librosa.result()
