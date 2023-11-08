from sqlalchemy import create_engine, func
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///music.db')

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'<Artist(id={self.id}, name={self.name})>'

class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    def __repr__(self):
        return f'<Album(id={self.id}, title={self.title})>'

class Track(Base):
    __tablename__ = 'tracks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    album_id = Column(Integer, ForeignKey('albums.id'))

    def __repr__(self):
        return f'<Track(id={self.id}, title={self.title})>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)