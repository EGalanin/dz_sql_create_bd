from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, ForeignKey, Numeric, SmallInteger, VARCHAR, DECIMAL

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker
import psycopg2
from pprint import pprint

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://admin_:pass@localhost:5432/music")
Session = sessionmaker(bind=engine)
session = Session()


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(40), nullable=False)
    ganres = relationship('Ganre', secondary='artist_genre')
    albums = relationship('Album', secondary='album_artist')


artist_genre = Table('artist_genre', Base.metadata,
                     Column('genre_id', Integer, ForeignKey('genre.id')),
                     Column('artist_id', Integer, ForeignKey('artist.id')))


class Ganre(Base):
    __tablename__ = "ganre"
    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    ganre_name = Column(VARCHAR(40), nullable=False)
    artists = relationship('Artist', secondary='artist_genre')


class Album(Base):
    __tablename__ = "album"
    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    album_name = Column(VARCHAR(40), nullable=False)
    years = Column(Integer)
    # tracks = relationship('Track', backref='album', uselist=False)
    artists = relationship('Artist', secondary='album_artist')


album_artist = Table('album_artist', Base.metadata,
                     Column('album_id', Integer, ForeignKey('album.id')),
                     Column('artist_id', Integer, ForeignKey('artist.id')))


class Track(Base):
    __tablename__ = "track"
    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    track_name = Column(VARCHAR(60), nullable=False)
    track_time = Column(DECIMAL)

    album_id = Column(Integer, ForeignKey('album.id'))
    album = relationship('Album', backref='track', uselist=False)
    collections = relationship('Collection', secondary='collection_track')


class Collection(Base):
    __tablename__ = "collection"
    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    collection_name = Column(VARCHAR(60), nullable=False)
    years = Column(Integer)
    tracks = relationship('Track', secondary='collection_track')


collection_track = Table('collection_track', Base.metadata,
                         Column('collection_id', Integer, ForeignKey('collection.id')),
                         Column('track_id', Integer, ForeignKey('track.id')))

if __name__ == '__main__':
    session = Session()
    Base.metadata.create_all(engine)


# session.commit()

# artists_data = [
#     {'artist': 'Limp Bizkit',
#      'genres': ['rock', 'hip-hop', 'metal'],
#      'albums': [{'album': 'Chocolate Starfish and the Hot Dog Flavored Water',
#                  'year': 2000,
#                  'tracks': [{'track': 'My Generation', 'continuity': 221},
#                             {'track': 'My Way', 'continuity': 273},
#                             {'track': 'Rollin’ (Air Raid Vehicle)', 'continuity': 214},
#                             {'track': 'Take a Look Around', 'continuity': 318}
#                             ]
#                  },
#                 {'album': 'Results May Vary',
#                  'year': 2003,
#                  'tracks': [{'track': 'Re-Entry', 'continuity': 157},
#                             {'track': 'Eat You Alive', 'continuity': 237},
#                             {'track': 'Gimme The Mic', 'continuity': 185},
#                             {'track': 'Underneath The Gun', 'continuity': 342},
#                             {'track': 'Down Another Day', 'continuity': 246},
#                             {'track': 'Build A Bridge', 'continuity': 278},
#                             {'track': 'Red Light-Green Light', 'continuity': 237},
#                             {'track': 'The Only One', 'continuity': 336},
#                             {'track': 'Behind Blue Eyes', 'continuity': 365}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Lera Lynn',
#      'genres': ['rock', 'country', 'folk'],
#      'albums': [{'album': 'The Avenues',
#                  'year': 2014,
#                  'tracks': [{'track': 'Standing on the Moon', 'continuity': 260},
#                             {'track': 'Coming down', 'continuity': 232},
#                             {'track': 'Hooked on You', 'continuity': 237},
#                             {'track': 'Sailor Song', 'continuity': 240}
#                             ]
#                  },
#                 {'album': 'Resistor',
#                  'year': 2016,
#                  'tracks': [{'track': 'Shape Shifter', 'continuity': 231},
#                             {'track': 'What You Done', 'continuity': 236},
#                             {'track': 'Scratch + Hiss', 'continuity': 297}
#                             ]
#                  },
#                 {'album': 'Plays Well With Others',
#                  'year': 2018,
#                  'tracks': [{'track': 'Lose Myself', 'continuity': 210},
#                             {'track': 'Crimson Underground', 'continuity': 189},
#                             {'track': 'In Another Life', 'continuity': 212}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Lady Gaga',
#      'genres': ['pop', 'hip-hop'],
#      'albums': [{'album': 'Born This Way',
#                  'year': 2014,
#                  'tracks': [{'track': 'Judas', 'continuity': 262},
#                             {'track': 'Americano', 'continuity': 246},
#                             {'track': 'Hair', 'continuity': 250},
#                             {'track': 'Bad Kids', 'continuity': 231}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Metallica',
#      'genres': ['rock', 'metal'],
#      'albums': [{'album': 'Black Album',
#                  'year': 1991,
#                  'tracks': [{'track': 'Enter Sandman', 'continuity': 330},
#                             {'track': 'Sad but True', 'continuity': 323},
#                             {'track': 'The Unforgiven', 'continuity': 227},
#                             {'track': 'Nothing Else Matters', 'continuity': 386}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': '50 Cent',
#      'genres': ['hip-hop'],
#      'albums': [{'album': 'The Massacre',
#                  'year': 2005,
#                  'tracks': [{'track': 'In My Hood', 'continuity': 231},
#                             {'track': 'This Is 50', 'continuity': 184},
#                             {'track': 'Piggy Bank', 'continuity': 255}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Eminem',
#      'genres': ['hip-hop'],
#      'albums': [{'album': 'The Marshall Mathers LP',
#                  'year': 2000,
#                  'tracks': [{'track': 'Stan', 'continuity': 344},
#                             {'track': 'Marshall Mathers', 'continuity': 321},
#                             {'track': 'Under the Influence', 'continuity': 322}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Dido',
#      'genres': ['hip-hop'],
#      'albums': [{'album': 'The Marshall Mathers LP',
#                  'year': 2000,
#                  'tracks': [{'track': 'Stan', 'continuity': 344}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Iggy Pop',
#      'genres': ['rock'],
#      'albums': [{'album': 'The Idiot',
#                  'year': 1977,
#                  'tracks': [{'track': 'Sister Midnight', 'continuity': 263},
#                             {'track': 'Nightclubbing', 'continuity': 258},
#                             {'track': 'Funtime', 'continuity': 173},
#                             {'track': 'Baby', 'continuity': 200}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Johny Cash',
#      'genres': ['rock', 'country', 'folk'],
#      'albums': [{'album': 'American III: Solitary Man',
#                  'year': 2000,
#                  'tracks': [{'track': 'Solitary Man', 'continuity': 205},
#                             {'track': 'One', 'continuity': 233},
#                             {'track': 'I See a Darkness', 'continuity': 222},
#                             {'track': 'Country Trash', 'continuity': 107}
#                             ]
#                  }
#                 ]
#      },
#     {'artist': 'Disturbed',
#      'genres': ['metal'],
#      'albums': [{'album': 'The Sickness',
#                  'year': 2000,
#                  'tracks': [{'track': 'Stupify', 'continuity': 274},
#                             {'track': 'Down with the Sickness', 'continuity': 278},
#                             {'track': 'Violence Fetish', 'continuity': 203}
#                             ]
#                  },
#                 {'album': 'Believe',
#                  'year': 2002,
#                  'tracks': [{'track': 'Prayer', 'continuity': 221},
#                             {'track': 'Liberate', 'continuity': 209},
#                             {'track': 'Awaken', 'continuity': 269}
#                             ]
#                  }
#                 ]
#      }
# ]
#
# for i in artists_data:
#     artist_item = Artist(name=['artist'])
#     # artist_id = session.query('Artist').filter(Artist.name == ['artist'])
#     ganre_item = Ganre(ganre_name=['ganres'])
#     # ganre_id = session.query('Ganre').filter(Ganre.ganre_name == ['ganres'])
#     for album in i['albums']:
#         album_item = Album(album_name=['album'], years=['year'], artists=['artist'])
#     track_list = []
#         for track in i['albums'][2]:
#             track_item = Track(track_name=['track'], track_time=['continuity'], album=['album'])
#             track_list.append(track_item)
# # session.add_all()
# session.commit()
