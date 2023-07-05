from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# excecuting the chinook database
db = create_engine("postgresql:///chinook")

# grab metadata and return subclass to map all back to us
base = declarative_base()


# tables
# class-based model for 'Artist' table

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# class-based model for 'Album' table

class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey(Artist.ArtistId))


# class-based model for 'Track' table

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey(Album.AlbumId))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Set instance of sessionmaker to use 'db'

Session = sessionmaker(db)

# Open session by using the Session subclass above & stores result

session = Session()

# Create database using the declarative_base subclass 'base'

base.metadata.create_all(db)

# Query 1 - 'Artist' instance

# artists = session.query(Artist)

# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - Select all names from the 'Artist' table

# artists = session.query(Artist)

# for artist in artists:
#     print(artist.Name)

# Query 3 - Select all data from the 'Artist' table where name = Queen

# artists = session.query(Artist).filter_by(Name="Queen").first()

# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - Select all records from the 'Artist' table where ArtistId = 51

# artists = session.query(Artist).filter_by(
#     ArtistId=51)  # use .first() & no for loop

# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - Select all records from the 'Album' table where ArtistId = 51

# albums = session.query(Album).filter_by(
#     ArtistId=51)  # use .first() & no for loop

# for album in albums:
#     print(
#         f'AlbumId: {album.AlbumId}, ArtistId: {album.ArtistId}, 
# Title: {album.Title}')

# Query 6 - Select all records from the 'Track'

# tracks = session.query(Track)

# for track in tracks:
#     print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId,
#           track.GenreId, track.Composer, track.Milliseconds,
# track.Bytes, track.UnitPrice, sep=' | ')


# Query 7 - Select all records from the 'Track'
# table where Composer = 'Queen'

tracks = session.query(Track).filter_by(Composer='Queen')
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice, sep=' | ')
