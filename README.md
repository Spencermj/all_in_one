# Problem
We want to combine all songs in a local directory into one .mp3 file.

# Question
1. How do you load a song from a local audio file?
2. How do you access all the songs from a certain directory?
3. How do you combine multiple songs into one .mp3?

# Resources
1. [LocalAudioFile Code]
2. [show_attrs.py]
3. [echonest.remix]

### 1. Loading local audio files with [LocalAudioFile Code]
The code for echonest.remix.audio.LocalAudioFile shows how to create a LocalAudioFile object if given the path of a song. The following code creates a single LocalAudioFile object:
```python
import echonest.remix.audio as audio
audiofile = audio.LocalAudioFile(input_filename)
```
This resource answers the question 1: how do you load a song from a local audio file?

### 2. Accessing all songs in a directory based off of [show_attrs.py]
From this code I'm using the `show_attrs` method to recursively access each song in a directorry. The following code from the `show_attrs` method prints all the attributes of each song in a given directory: 
```python
import os
for f in os.listdir(directory):
        if _is_audio(f):
            path = os.path.join(directory, f)
            _show_one(path)
```
By removing the portion of the code that prints the attributes of each song, specifically the _show_one() function, I have the necessary code to access each individual audio file in a directory. The _is_audio() function is also required to make sure each individual file accessed is an audio file, but this can be accomplished with the following code:
```python
AUDIO_EXTENSIONS = set(['mp3', 'm4a', 'wav', 'ogg', 'au', 'mp4'])
_, ext = os.path.splitext(f)
    ext = ext[1:] # drop leading '.'
    return ext in AUDIO_EXTENSIONS
This resource answers question 2: how do you access all the songs from a certain directory?

### 3. Combining songs using [echonest.remix]
Remix allows you to form AudioQuantumList objects made from AudioQuantum objects, this means that you can make a list of segments, beats, tatums, etc. By breaking each song I analyze into segments and appending the segments of each song onto an AudioQuantumList object, I can essentially create one song that is made up of all the segments from each individual song. 

[LocalAudioFile Code]: http://echonest.github.io/remix/apidocs/echonest.remix.audio.LocalAudioFile-class.html
[show_attrs.py]: https://github.com/echonest/pyechonest/blob/master/examples/show_attrs.py
[echonest.remix]: http://echonest.github.io/remix/tutorial.html
