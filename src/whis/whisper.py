import pyaudio
import wave
from openai import OpenAI

import sys
from pathlib import Path
from os import getenv, remove

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5

client = OpenAI()

def main():

    path = str(Path(__file__).parent.resolve()) + "/"
    audio_location = path + "audio.wav"

    if len(sys.argv)>3:
        print("Too many arguments")
        return

    if len(sys.argv)==2 or len(sys.argv)==3:
        file_path = sys.argv[1].strip()
        if len(sys.argv)==3:
            prompt = sys.argv[2].strip()
            print("\n" + whisper(file_path, prompt))
        else:
            print("\n"+ whisper(file_path))

        
    else:
        record(audio_location)
        print(whisper(audio_location))
        remove(audio_location)
        

def record(audio_location):
    with wave.open(audio_location, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print("\033[1;31mRecording 🎶 (press C-c to stop)\033[0m")
        try:
            while True: 
                wf.writeframes(stream.read(CHUNK))
        except KeyboardInterrupt:
            print("\r  ")

        stream.close()
        p.terminate()

def whisper(file, prompt=""):
    if not getenv("OPENAI_API_KEY"):
        print("No environment variable found")
        exit()
    client.api_key = getenv("OPENAI_API_KEY")
    with open(file, "rb") as audio_file:
        try:
            transcript = client.audio.transcriptions.create(
                    model = "whisper-1",
                    file = audio_file,
                    prompt = prompt).text
        except:
            transcript = "Oops, that didn't work"
    return transcript

if (__name__)=="__main__":
    main()
