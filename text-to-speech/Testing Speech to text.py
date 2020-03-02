# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:45:54 2020

@author: Saurabh
"""
#%%
import speech_recognition as sr;
from os import path;


#%%
# case 1: recognizing and converting live audio using laptop Microphone to text

# step 1: listen to audio file from microphone source
recognizer_microphone = sr.Recognizer()
with sr.Microphone() as source:
    print("start talking");
    input_audio = recognizer_microphone.listen(source);
#%%
# step 2: pring text from audio after analysis
try:
    print("What do you mean by :");
    print(recognizer_microphone.recognize_sphinx(input_audio));
except sr.UnknownValueError:
    print("Sphinx could not understand audio");
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e));

#%%    
# case 2: recognizing and converting a audio file to text
    
# step 1: load audio file
audio_files_location = 'F:/Workspace-Personal/Improvements-workspace/semicolons-2020/Speech-to-text-converter/recordings/';
audio_file_name =  'Recording.m4a';

from pydub import AudioSegment

#%%
def conver_m4a_to_wav():
    src = "Recording.mp3"
    dest = "test.wav"                                                 
    sound = AudioSegment.from_mp3(path.join(audio_files_location,src))
    sound.export(path.join(audio_files_location,dest), format="wav")

#%%    
AUDIO_FILE = path.join(audio_files_location, audio_file_name);
#%%
conver_m4a_to_wav()
#%%
# step 2: recognizer entire saved audio file 
recognizer_audiofile = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = recognizer_audiofile.record(source)
#%%
