
ALTER TABLE tracks ALTER COLUMN treck_time NUMERIC(1,2) NOT NULL;

INSERT INTO albums (album_name, years)
VALUES ('album_1', 2018),
	   ('album_2', 2012),
	   ('album_3', 2020),
	   ('album_4', 2006),
	   ('album_5', 2018),
	   ('album_6', 1992),
	   ('album_7', 2022),
	   ('album_8', 1983);
	  
INSERT	INTO ganre(ganre_name)
VALUES ('rock'),
	   ('hip-hop'),
	   ('metal'),
	   ('country'),
	   ('folk');
	  
	  
INSERT INTO artists	(nickname)  
VALUES ('nickname_1'),
	   ('nickname_2'),
	   ('nickname_3'),
	   ('nickname_4'),
	   ('nickname_5'),
	   ('nickname_6'),
	   ('nickname_7'),
	   ('nickname_8');
	  
INSERT	INTO tracks(track_name, treck_time) 
VALUES ('track_1', 2.15),
       ('track_2', 3.28),
       ('track_3', 3.15),
       ('track_4', 2.37),
       ('track_5', 4.46),
       ('track_6', 6.15),
       ('track_7', 1.55),
       ('track_8', 3.48),
       ('track_9', 3.54),
       ('track_10', 2.33),
       ('track_11', 3.22),
       ('track_12', 4.18),
       ('my_best_track', 3.47),
       ('track_my', 2.17),
       ('top_my_track', 4.07);
      
 INSERT INTO collection (collection_name, years) 
 VALUES ('collection_1', 2020),
        ('collection_2', 2012),
        ('collection_3', 2018),
        ('collection_4', 2015),
        ('collection_5', 2012),
        ('collection_6', 2020),
        ('collection_7', 2011),
        ('collection_8', 2008);
        
INSERT INTO albums_artists(artist_id, albums_id)
VALUES (9, 1),
	   (9, 4),
	   (10, 2),
	   (11, 3),
	   (12, 2),
	   (12, 5),
	   (13, 8),
	   (14, 3),
	   (14, 6),
	   (15, 7),
	   (16, 6),
	   (16, 8);
	  
INSERT INTO artists_ganres(ganre_id, artist_id)
VALUES (1, 10),
       (1, 12),
	   (1, 14),
       (2, 9),
	   (2, 12),
       (3, 10),
	   (3, 15),
       (4, 11),
	   (4, 16),
       (5, 11),
	   (5, 13),
       (5, 15);
	  
 INSERT INTO collection_tracks(collection_id, track_id)
 VALUES (1,1),
        (1, 5),
	    (1, 14),
        (1, 8),
	    (2, 2),
        (2, 5),
	    (2, 11),
        (3, 4),
	    (3, 13),
        (3, 6),
	    (3, 8),
        (4, 2),
	    (4, 10),
        (4, 9),
	    (5, 3),
        (5, 7),
	    (5, 12),
        (5, 14),
	    (6, 1),
        (6, 8),
	    (6, 11),
        (6, 12),
	    (7, 6),
        (7, 1),
	    (7, 13),
        (8, 2),
	    (8, 8),
        (8, 3),
	    (8, 11),
        (8, 13);
       

	   
