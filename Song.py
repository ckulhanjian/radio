class Song:
    def __init__(self, title, artist, album, year):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
    
    def get_song(self):
        return {"title": self.title, "artist": self.artist, "album": self.album, "year": self.year}