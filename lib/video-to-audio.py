import os
import pathlib
import moviepy.editor as mp
from random import random
import os.path

def convert(filename):
    clip = mp.VideoFileClip(filename)
    outputFile ="audio-" + str(int(random()*100)) + ".wav"
    clip.audio.write_audiofile(outputFile)
'''
#function to generate a unique file
def generateFilename():
    outputDirectory = "../converted/"
    fileName = "audio-" + str(int(random()*100)) + ".wav"
	if (!os.path.exists("../converted"+fileName)):
		return outputDirectory + fileName
	else:
		fileName = "audio-" + str(int(random()*100)) + ".wav"
'''