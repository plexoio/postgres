import psycopg2  # data adapter

# connect to database
connection = psycopg2.connect(database="chinook")

# build cursor object of the DB | another name for 'set', list' or 'array'
cursor = connection.cursor()

# Query 1 - Select all records from the 'Artist' table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select all names from the 'Artist' table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select all data from the 'Artist' table where name = Queen
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aerosmith"])

# Query 4 - Select all records from the 'Artist' table where ArtistId = 51
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [50])

# Query 5 - Select all records from the 'Album' table where ArtistId = 51
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [3])

# Query 6 - Select all records from the 'Album' table where ArtistId = 51
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen']) 
# we can add more

# fetchall
results = cursor.fetchall()

# fetch single
# results = cursor.fetchone()

# close connection
connection.close()

# print results
for result in results:
    print(result)
    if result[0] == 5:
        print(f'\nMy prefered result: {result[1]}\n')
