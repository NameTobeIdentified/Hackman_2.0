import json
from watson_developer_cloud import SpeechToTextV1
import moviepy.editor as mp

clip = mp.VideoFileClip("sample_interview.mp4").subclip(94,137)
clip.audio.write_audiofile("theaudio.wav")
service = SpeechToTextV1(
    url = 'https://gateway-syd.watsonplatform.net/speech-to-text/api',
    iam_apikey = 'GxPN0hJ8oFWvOslvJ3t10S3-GcBf1vY1Ut1fFi4psNHA'
)

with open('./theaudio.wav','rb') as audio_file:
    output = json.dumps(
        service.recognize(
            audio=audio_file,
            content_type='audio/wav',
            timestamps=True,
            speaker_labels=True,
            word_confidence=True).get_result(),
            indent=2)

output_dict = json.loads(output)
print(output_dict['results'][0]['alternatives'][0]['transcript'])

speakers = set()
for i in output_dict['speaker_labels']:
    speakers.add(i['speaker'])
print(speakers)
speakers = list(speakers)

timestamps = output_dict['results'][0]['alternatives'][0]['timestamps']

speaker_timestamps = output_dict['speaker_labels']

current_speaker = 0
print('Speaker',speakers[0],':', end = " ")
for i,j in zip(timestamps,speaker_timestamps):
    if ( (i[1],i[2]) == (j['from'],j['to']) ):
        if j['speaker'] != current_speaker:
            current_speaker = j['speaker']
            print('\nSpeaker', j['speaker'],':',i[0], end =" ")
            
        elif j['speaker'] == current_speaker:
            print(i[0], end =" ")