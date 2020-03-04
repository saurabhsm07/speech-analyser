# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:45:54 2020

@author: Saurabh
"""
#%%
import speech_recognition as sr;
from os import path;
from pydub import AudioSegment
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")
#%%

class Speech_analyser:
    audio_files_location = 'F:/Workspace-Personal/Improvements-workspace/semicolons-2020/Speech-to-text-converter/recordings/';
    input_audio_filename =  '';
    processed_audio_filename = '';
    speech_to_text_result = '';
    
    def set_input_file_name(self, filename):
        self.input_audio_filename = filename;
        
    def convert_m4a_to_wav(self):
        src = self.input_audio_filename;
        dest = self.input_audio_filename.split('.')[0] + 'wav';
        try:                                                 
            sound = AudioSegment.from_file(path.join(self.audio_files_location,src), format = 'mp4');
            sound.export(path.join(self.audio_files_location,dest), format = 'wav');
            self.processed_audio_filename = dest;
        except:
            self.processed_audio_filename = "file_error";
        
    def convert_mp3_to_wav(self):
        src = self.input_audio_filename;
        dest = self.input_audio_filename.split('.')[0] + 'wav';
        try:                                                 
            sound = AudioSegment.from_file(path.join(self.audio_files_location,src), format = 'mp3');
            sound.export(path.join(self.audio_files_location,dest), format = 'wav');
            self.processed_audio_filename = dest;
        except:
            self.processed_audio_filename = "file_error";
    
    def analyse_live_audio(self):
        recognizer_microphone = sr.Recognizer()
        with sr.Microphone() as source:
            print("start talking");
            microphone_audio = recognizer_microphone.listen(source);
        self.convert_speech_to_text(microphone_audio, recognizer_microphone);
    
    def analyse_audio_file(self):
        format = self.input_audio_filename.split(".")[1];
        if format == 'wav':
            self.analyse_file()
        elif format == 'mp3':
            self.convert_mp3_to_wav();
            self.analyse_file();
        elif format == 'm4a':
            self.convert_m4a_to_wav();
            self.analyse_file();
        else:
            print("can't decode file of format = {}".format(format));
    
    def analyse_file(self):
        if(self.processed_audio_filename == "file_error"):
            print("error in file conversion")
        else:
            recognizer_audiofile = sr.Recognizer();
            audio_file = path.join(self.audio_files_location, self.processed_audio_filename);
            with sr.AudioFile(audio_file) as source:
                file_audio = recognizer_audiofile.record(source);
            self.convert_speech_to_text(file_audio, recognizer_audiofile);
        
    def convert_speech_to_text(self, audio, recognizer):
        try:
            print("What do you mean by :");
            print(recognizer.recognize_sphinx(audio));
        except sr.UnknownValueError:
            print("Sphinx could not understand audio");
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e));

    def audio_to_text(self):
        if self.speech_to_text_result == "":
            print("nothing analysed");
        else:
            print("speech analysis results :");
            print(self.speech_to_text_result);



#%%
analyser = Speech_analyser()                    #initialize analyser object
#%%
analyser.set_input_file_name('Recording.m4a')   #set file name to be processed
#%%
analyser.analyse_audio_file()                   #analyse audio function
#%%
