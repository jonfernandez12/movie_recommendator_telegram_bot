from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

Base = declarative_base()

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(String)
    link = Column(String)
    rating = Column(String)
    runtime = Column(String)
    genre = Column(String)
    plot = Column(String)
    status = Column(Integer)
    recomendation = relationship("Recomendation")

    def __init__(self, title, year, link, rating, runtime, genre, plot, status):        
        self.title = title
        self.year = year
        self.link = link
        self.rating = rating
        self.runtime = runtime
        self.genre = genre
        self.plot = plot
        self.status = status

        super(Film, self).__init__()

    def __repr__(self):
        return "<Film(id='{}',title='{}', year='{}', link='{}', rating='{}', runtime'{}', genre'{}', plot'{}', status'{}')>"\
                .format(self.id, self.title, self.year, self.link, self.rating, self.runtime, self.genre, self.plot, self.status)
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recomendation = relationship("Recomendation")


    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.filmId = ""
        super(User, self).__init__()

    def __repr__(self):
        return "<user(id='{}', name'{}', filmId='{}')>"\
                .format(self.id, self.name, self.filmId)


class Recomendation(Base):
    __tablename__ = 'recomendations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    filmId = Column(Integer, ForeignKey('films.id'))


    def __init__(self, id, title, filmId):
        self.userId = id
        self.name = title
        self.filmId = filmId
        super(User, self).__init__()

    def __repr__(self):
        return "<user(id='{}',userId'{}', name'{}', filmId='{}')>"\
                .format(self.id,self.userId,  self.name, self.filmId)