import pyaudio
import wave
import openai
import sys
from pynput import keyboard
from pathlib import Path
from os import getenv

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5


def main():

    path = str(Path(__file__).parent.resolve()) + "/"
    audio_location = path + "audio.wav"

    if len(sys.argv)>2:
        print("Too many arguments")
        return

    if len(sys.argv)==2:
        print("\n"+ whisper(sys.argv[1].strip()))
        
    else:
        record(audio_location)
        print(whisper(audio_location))
        

def record(audio_location):
    with wave.open(audio_location, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print("Recording 🎶 (press C-c to stop)")
        try:
            while True: 
                wf.writeframes(stream.read(CHUNK))
        except KeyboardInterrupt:
            pass
        print()

        stream.close()
        p.terminate()

def whisper(file):
    if not getenv("OPENAI_API_KEY"):
        print("No environment variable found")
        exit()
    openai.api_key = getenv("OPENAI_API_KEY")
    audio_file = open(file, "rb")
    transcript = openai.Audio.transcribe(
            model = "whisper-1",
            file = audio_file,
            prompt = "The following video is by the Primeagen, contains mulitple paragraphs of content.\n\nLike this for example.")["text"]
    return transcript

if (__name__)=="__main__":
    main()
