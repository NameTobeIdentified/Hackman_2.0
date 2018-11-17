import os
import moviepy.editor as mp
from random import random

def convert(filename):
    clip = mp.VideoFileClip(filename)
    outputFile = generateFilename()
    clip.audio.write_audiofile(outputFile)

def generateFilename():
    outputDirectory = "../converted/"
    fileName = "audio" + str(int(random()*100)) + ".wav"
    for root, dirs, files in os.walk("../converted"):  
        for file in files:
            if fileName !=  file:
                return outputDirectory + fileName
            else:
                fileName = "audio" + str(int(random()*100)) + ".wav"