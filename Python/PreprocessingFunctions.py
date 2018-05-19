import pandas as fluff
import csv
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions
import pandas as pd
def getSongParts():
    song_parts = fluff.read_csv('songs_parts.csv',sep=',', encoding = "ISO-8859-1")

    with open('song_chorus.csv', 'w') as csvfile:
        sentiment_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sentiment_writer.writerow(["id", "text"])
        for i in range(len(song_parts.index)):
            try:
                an_chorus = song_parts.loc[i, 'chorus']
                song_title = song_parts.loc[i, 'Song Title']
                sentiment_writer.writerow([song_title,an_chorus])
            except Exception as e:
                print(e)

    with open('song_verse.csv', 'w') as csvfile:
        sentiment_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sentiment_writer.writerow(["id", "text"])
        for i in range(len(song_parts.index)):
            try:
                verse = song_parts.loc[i, 'verse']
                song_title = song_parts.loc[i, 'Song Title']
                sentiment_writer.writerow([song_title,verse])
            except Exception as e:
                print(e)
def mergAudioandTextualfeatures():
    audio_features = pd.read_csv('audio_features.csv',error_bad_lines=False)
    all_emotions = pd.read_csv('all_features.csv',error_bad_lines=False, encoding="ISO-8859-1")
    merged_allfeatures = pd.merge(audio_features,all_emotions, how='left', on='Song Title')
    merged_allfeatures.to_csv('all_features.csv', index=False)
def getEmotionsinChorus():
    sp = pd.read_csv('alive-musicians.csv', sep=',', encoding = "ISO-8859-1")
    chorus_part = sp.chorus


    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username='1c0beaf1-fd39-4332-84bc-771391b4966d',
      password='OzrVxY66aihC',
      version='2017-02-27')

    with open('sentiment_alive_c.csv', 'w') as csvfile:
        sentiment_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sentiment_writer.writerow(["Artist", "Song Title", "sadness","joy","fear","disgust","anger"])
        for i in range(len(sp.index)):
            try:
                an_chorus = sp.loc[i, 'chorus']
                artist = sp.loc[i, 'Artist']
                song_title = sp.loc[i, 'Song Title']
                #try:
                response = natural_language_understanding.analyze(
                    text= an_chorus,
                    features=Features(
                    emotion=EmotionOptions()))
                response = response['emotion']['document']
                print(response)
                #except Exception as e:
                    #print('ERROR')
                sentiment_writer.writerow([artist, song_title, response['emotion']['sadness'],response['emotion']['joy'],response['emotion']['fear'],response['emotion']['disgust'],response['emotion']['anger']])
            except Exception as e:
                print(e)
                
def getEmotionsinVerse():
    sp = pd.read_csv('alive-musicians.csv', sep=',', encoding = "ISO-8859-1")
    chorus_part = sp.verse

    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username='1c0beaf1-fd39-4332-84bc-771391b4966d',
      password='OzrVxY66aihC',
      version='2017-02-27')

    with open('sentiment_alive_v.csv', 'w') as csvfile:
        sentiment_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sentiment_writer.writerow(["Artist", "Song Title", "sadness","joy","fear","disgust","anger"])
        for i in range(len(sp.index)):
            try:
                an_verse = sp.loc[i, 'verse']
                artist = sp.loc[i, 'Artist']
                song_title = sp.loc[i, 'Song Title']
                #try:
                response = natural_language_understanding.analyze(
                    text= an_verse,
                    features=Features(
                    emotion=EmotionOptions()))
                response = response['emotion']['document']
                print(response)
                #except Exception as e:
                    #print('ERROR')
                sentiment_writer.writerow([artist, song_title, response['emotion']['sadness'],response['emotion']['joy'],response['emotion']['fear'],response['emotion']['disgust'],response['emotion']['anger']])
            except Exception as e:
                print(e)
