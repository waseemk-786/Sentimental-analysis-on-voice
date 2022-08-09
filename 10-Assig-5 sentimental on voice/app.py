import streamlit as st
import boto3
import speech_recognition as sr
from pydub import AudioSegment


st.title("Sentimental analysis on voice with AWS")
voice_file = st.file_uploader('Upload WAV File')

if voice_file is not None:
    if st.button("Predict"):
        # initialize the recognizer
        r = sr.Recognizer()
        with sr.AudioFile(voice_file) as source:
       # listen for the data (load audio to memory)
         audio_data = r.record(source)
        # recognize (convert from speech to text)
         text = r.recognize_google(audio_data)
         

        client=boto3.client('comprehend')
        response=client.detect_sentiment(
        Text=text,
        LanguageCode='en'
        )
        if(response['Sentiment']=='POSITIVE'):
             st.success("Positive response")
        elif (response['Sentiment']=='NEGATIVE'):
             st.error('Negative response')
        elif (response['Sentiment']=='NEUTRAL'):
             st.warning('Neutral response')
        else:
             st.write("Mixed text")
    