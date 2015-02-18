import echonest.remix.audio as audio
import sys
import os

AUDIO_EXTENSIONS = set(['mp3', 'm4a', 'wav', 'ogg', 'au', 'mp4'])

def main(directory, output_filename):
    collect = []
    recurseThroughDirectory(directory, collect)
    out = audio.assemble(collect)
    out.encode(output_filename)

def recurseThroughDirectory(directory, audioDataList):
    for f in os.listdir(directory):
        if _isAudio(f):
            path = os.path.join(directory, f)
            _addOneSong(path, audioDataList)

def _addOneSong(path, audioDataList):
    audiofile = audio.LocalAudioFile(path)
    audioDataList.append(audiofile)

def _isAudio(f):
    _, ext = os.path.splitext(f)
    ext = ext[1:] 
    return ext in AUDIO_EXTENSIONS

if __name__ == '__main__':
    try:
        directory = sys.argv[1]
        output_filename = sys.argv[2]
    except:
        print usage
        sys.exit(-1)
    main(directory, output_filename)


