# Vocalist

This is a simple project still in very early development, meant to be used to parse speech into text.  In its current state, it only works on Mac, and only where a compatible version of [PortAudio](http://www.portaudio.com/) has been installed.

It was built following the tutorial found here: [https://realpython.com/python-speech-recognition/](https://realpython.com/python-speech-recognition/)

## Setup

Using Homebrew, install PortAudio:
```bash
$ brew install portaudio 
```

From there you can install dependencies as you normally would:
```bash
$ pip install -r requirements.txt
```

## Usage

If you want to call it directly just run the package as is:
```bash
$ python ./main.py
``` 

It's not currently deployed for package management.