
ALTER TABLE tracks ALTER COLUMN treck_time TYPE numeric(10,2);

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
VALUES ('nick name_1'),
	   ('nick name_2'),
	   ('nickname_3'),
	   ('nick name_4'),
	   ('nick name_5'),
	   ('nick name_6'),
	   ('nick name_7'),
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
        