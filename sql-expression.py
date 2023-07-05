from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

db = create_engine("postgresql:///chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

with db.connect() as connection:
    # Query 1 - Select all records from the 'Artist' table
    # select_query = artist_table.select()

    # Query 2 - Select all names from the 'Artist' table
    # select_query = artist_table.select().with_only_columns(
    #     [artist_table.c.Name])

    # Query 3 - Select all data from the 'Artist' table where name = Queen
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Query 4 - Select all records from the 'Artist' table where ArtistId = 51
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - Select all records from the 'Album' table where ArtistId = 51
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all records from the 'Track'
    # table where Composer = 'Queen'
    select_query = track_table.select().where(
        track_table.c.Composer == 'Queen')

    # Query 7 - Select all records from the 'Track' table

    # select_query = track_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
