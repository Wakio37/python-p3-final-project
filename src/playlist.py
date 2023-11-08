from sqlalchemy import create_engine, func
from models import Track, Album, Artist
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///music.db')


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class Playlist:
    @staticmethod
    def add_track( title):
        session = get_session()
        track = Track(title=title)
        session.add(track)
        session.commit()
    @staticmethod
    def remove_track(title):
        session = get_session()
        track = session.query(Track).filter_by(title=title).first()
        session.delete(track)
        session.commit()

    @staticmethod
    def get_all_tracks():
        session = get_session()
        tracks = session.query(Track).all()
        return tracks
