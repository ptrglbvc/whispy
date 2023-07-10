# whispy

## What is it?
A tool for transcribing text built on OpenAI's whisper 1 model in the terminal. 

## What are the dependencies?
Other than _Python 3.0+_ and the libraries included in the **setup.py** file, it also needs [PortAudio 19](https://github.com/PortAudio/portaudio).

## How to set it up?
After installing dependencies, clone this repo.
```
git clone https://github.com/ptrglbvc/whispy
```
Change directory to the folder.
```
cd whispy
```
Install it with pip in editable mode. If anyone knows how to make it work in regular install, I would be very grateful.
```
pip install -e .
```
Add your API key in your environment variables in the .zshrc or .bashrc file.
```
export OPENAI_API_KEY = "(your key)"
```
In Windows, you just have to execute the following command in PowerShell.
```
$env:OPENAI_API_KEY = '(your key)' 
```

## How to use it?
For recording voice with your in-built microphone, just press wh from anywhere in the terminal. When the _Recording_ text shows up, you may start speaking. 
```
wh
```
If you want to transcribe an audio or video file, just provide it's absolute file location. (tip: you can just drag and drop the file to the command line in most terminals)
``` 
wh ~/Desktop/ДЕРЬМО.mp4
```
Output:
``` 
Нет! Нет! Нет! Дерьмо! Этого не может быть! Просто не может быть!
```
You can also provide a prompt to guide the model in the text formatting.
``` 
wh ~/Desktop/ДЕРЬМО.mp4 "THE Text shOUld LoOk lIKe THiS."
```
The prompt doesn't always work as it should in whisper v1, so I recommend using it sparingly.