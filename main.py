import sqlalchemy
import psycopg2
from pprint import pprint

engine = sqlalchemy.create_engine("postgresql+psycopg2://sanysh:pass@localhost:5432/music_servis")
#pprint((engine))
with engine.connect() as connection:

    # # название и год выхода альбомов, вышедших в 2018 году
    # select_1 = connection.execute('''SELECT album_name, years
    #                                  FROM albums
    #                                  WHERE years = 2018;''').fetchall()
    # pprint(select_1)
    # print('________________________________________________________')
    #
    # # название и продолжительность самого длительного трека
    # select_2 = connection.execute('''SELECT track_name, treck_time
    #                                  FROM tracks
    #                                  WHERE treck_time = (SELECT MAX(treck_time) FROM tracks);''').fetchone()
    # pprint(select_2)
    # print('________________________________________________________')
    #
    # # название треков, продолжительность которых не менее 3,5 минуты
    # select_3 = connection.execute('''SELECT track_name
    #                                  FROM tracks
    #                                  WHERE treck_time >= 3.50;''').fetchall()
    # pprint(select_3)
    # print('________________________________________________________')
    #
    # # названия сборников, вышедших в период с 2018 по 2020 год включительно
    # select_4 = connection.execute('''SELECT collection_name
    #                                  FROM collection
    #                                  WHERE years BETWEEN 2018 AND 2020;''').fetchall()
    # pprint(select_4)
    # print('________________________________________________________')
    #
    # # исполнители, чье имя состоит из 1 слова
    # select_5 = connection.execute('''SELECT nickname
    #                                  FROM artists
    #                                  WHERE nickname NOT LIKE '%% %%';''').fetchall()
    # pprint(select_5)
    # print('________________________________________________________')
    #
    # # название треков, которые содержат слово "мой"/"my"
    # select_6 = connection.execute('''SELECT track_name
    #                                  FROM tracks
    #                                  WHERE track_name LIKE '%%my%%';''').fetchall()
    # pprint(select_6)
    # print('________________________________________________________')



    #

    # количество исполнителей в каждом жанре
    select_1 = connection.execute('''SELECT ganre_name, COUNT(ag.artist_id)
                                     FROM ganre
                                     JOIN artists_ganres ag ON ganre.id = ag.ganre_id
                                     GROUP BY ganre_name;''').fetchall()
    pprint(select_1)
    print('________________________________________________________')


    # количество треков, вошедших в альбомы 2019-2020 годов
    select_2 = connection.execute('''SELECT COUNT(*)
                                     FROM tracks tr
                                     JOIN albums a ON tr.album_id = a.id 
                                     WHERE years BETWEEN 2019 AND 2020;''').fetchall()
    pprint(select_2)
    print('________________________________________________________')

    # средняя продолжительность треков по каждому альбому
    select_3 = connection.execute('''SELECT album_name, ROUND(AVG(t.treck_time), 2)
                                         FROM albums a
                                         JOIN tracks t ON a.id = t.album_id 
                                         GROUP BY album_name;''').fetchall()
    pprint(select_3)
    print('________________________________________________________')

    # все исполнители, которые не выпустили альбомы в 2020 году
    select_4 = connection.execute('''SELECT DISTINCT nickname
                                         FROM artists ar
                                         JOIN albums_artists aa ON ar.id = aa.artist_id 
                                         JOIN albums a ON aa.albums_id = a.id
                                         WHERE years != 2020;''').fetchall()
    pprint(select_4)
    print('________________________________________________________')

    # названия сборников, в которых присутствует конкретный исполнитель ('nickname_3')
    select_5 = connection.execute('''SELECT collection_name
                                         FROM collection c
                                         JOIN collection_tracks ct ON  c.id = ct.collection_id
                                         JOIN tracks tr ON ct.track_id = tr.id
                                         JOIN albums al ON tr.album_id = al.id
                                         JOIN albums_artists aa ON al.id = aa.albums_id
                                         JOIN artists ar ON aa.artist_id = ar.id
                                         WHERE ar.nickname LIKE 'nickname_3';''').fetchall()
    pprint(select_5)
    print('________________________________________________________')

    #название альбомов, в которых присутствуют исполнители более 1 жанра
    select_6 = connection.execute('''SELECT DISTINCT album_name
                                        FROM albums a
                                        JOIN albums_artists aa ON a.id = aa.albums_id
                                        JOIN artists ar ON aa.artist_id = ar.id
                                        JOIN artists_ganres ag ON ar.id = ag.artist_id
                                        GROUP BY ar.nickname, a.album_name
                                        HAVING count(ag.ganre_id) > 1;''').fetchall()

    pprint(select_6)
    print('________________________________________________________')

    # наименование треков, которые не входят в сборники
    select_7 = connection.execute('''SELECT track_name
                                        FROM tracks tr
                                        LEFT JOIN collection_tracks ct ON tr.id = ct.track_id
                                        WHERE ct.track_id is NULL;''').fetchall()



    pprint(select_7)
    print('________________________________________________________')

    # исполнителя(-ей), написавшего самый короткий по продолжительности трек (может быть несколько)
    select_8 = connection.execute('''SELECT nickname
                                        FROM artists ar
                                        JOIN albums_artists aa ON ar.id = aa.artist_id
                                        JOIN albums al ON aa.albums_id = al.id
                                        JOIN tracks tr ON al.id = tr.album_id
                                        WHERE tr.treck_time = (SELECT MIN(treck_time)
                                                                FROM tracks);''').fetchall()

    pprint(select_8)
    print('________________________________________________________')

    # название альбомов, содержащих наименьшее количество треков
    select_9 = connection.execute('''SELECT album_name, count(tr.id)
                                        FROM albums a
                                        JOIN tracks tr ON a.id = tr.album_id
                                        GROUP BY a.album_name
                                        HAVING count(tr.id) IN (SELECT count(tr.id)
                                                                FROM albums a
                                                                JOIN tracks tr ON a.id = tr.album_id
                                                                GROUP BY a.album_name
                                                                ORDER BY count(tr.id)
                                                                LIMIT 1)
                                                                
                                                                
                                        ORDER BY count(tr.id), album_name;''').fetchall()

    pprint(select_9)
    print('________________________________________________________')

