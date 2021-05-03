from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

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
