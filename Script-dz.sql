CREATE TABLE IF NOT EXISTS artists (
	id SERIAL PRIMARY KEY,
	nickname VARCHAR(40) NOT NULL UNIQUE
	);

CREATE TABLE IF NOT EXISTS ganre (
	id SERIAL PRIMARY KEY,
	ganre_name VARCHAR(40) NOT NULL 	
	);

CREATE TABLE IF NOT EXISTS artists_ganres (
	ganre_id INTEGER REFERENCES ganre(id),
	artist_id INTEGER REFERENCES artists(id),
	CONSTRAINT pk_artists_ganres PRIMARY KEY(ganre_id, artist_id)
	); 

CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	album_name VARCHAR(40) NOT NULL,
	years INTEGER
	);

CREATE TABLE IF NOT EXISTS albums_artists (
	artist_id INTEGER REFERENCES artists(id),
	albums_id INTEGER REFERENCES albums(id),
	CONSTRAINT pk_albums_artists PRIMARY KEY(artist_id, albums_id)
	);

CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY,
	track_name VARCHAR(60) NOT NULL,
	treck_time INTEGER NOT NULL,
	album_id INTEGER REFERENCES albums(id)
	);

CREATE TABLE IF NOT EXISTS collection (
	id SERIAL PRIMARY KEY,
	collection_name VARCHAR(60) NOT NULL,
	years INTEGER
	);

CREATE TABLE IF NOT EXISTS collection_tracks (
	collection_id INTEGER REFERENCES collection(id),
	track_id INTEGER REFERENCES tracks(id),
	CONSTRAINT pk_collection_tracks PRIMARY KEY(collection_id, track_id)
	); 