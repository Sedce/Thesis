song_parts = ['[verse]', '[chorus]','[intro]', '[outro]', '[bridge]']
emotions = {'anger': 1,'surprise' : 2,'sadness': 3, 'fear' : 4, 'joy': 5}

class Artist(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None):
        self.name = name
        self.song = []
        
    def addSong(self, song):
        self.song.append(song)
        
    def __repr__(self):
        return str(self)
    def getName(self):
        return self.name

#Song Object
import re
class Song(object):
            
        def __init__(self, name=None, lyrics = None):
            self.name = name
            self.chorus = []
            self.verse = []
            self.lyrics = []
        def getChorus(self):
            return self.chorus
        def getVerse(self):
            return self.verse
        def addLyrics(self, lyrics):
             #clean the lyrics
                self.lyrics = lyrics
                self._getParts(lyrics)
                return self
        def __repr__(self):
            return self
        def getName(self):
            return self.name
        def _getParts(self,lyrics):
            mark = 0
            if lyrics:
                for line in lyrics:
                    line = line.replace(',','')
                    line = line.rstrip()
                    print(line)
                    if (line == '[chorus]' or mark == 1) and  (line != '[verse]' and line != '[intro]' and line != '[outro]' and line != '[bridge]'):
                        print(line)
                        mark = 1
                        self.chorus.append(line)
                    elif (line == '[verse]' or mark == 2) and  (line != '[chorus]' and line != '[intro]' and line != '[outro]' and line != '[bridge]'):
                        mark = 2
                        self.verse.append(line)
                    else:
                        print('NO BRACKET')
                            
                            
        