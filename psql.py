import os
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import json
from models import Base, Film, User


CSV_FILE_PATH = os.getcwd()+'/Chatbot/movie_data.csv'
CONFIG_FILE_PATH = os.getcwd()+'/Chatbot/config.json'

def getCredentials():
    with open(CONFIG_FILE_PATH, "r") as file:
        conf = json.load(file)
    conn_string = conf["DATABASE_URI"]
    return conn_string

def insertFilms(db_session):
    with open(CSV_FILE_PATH) as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for i in reader:
            
            title = i[2]
            year = i[3]
            link = i[4]
            rating = i[5]
            runtime = i[6]
            genre = i[7]
            genre = genre + ', Random'
            plot = i[11]

            newFilm = Film(title,year,link,rating,runtime,genre,plot,0)

            db_session.add(newFilm)
            db_session.commit()
            #print(s.query(Film).first())
conn = None


def upsertUsers(db_session, user):
    id = user["id"]
    name = user["first_name"]
    newUser = User(id, name)
    exists = db_session.query(User.id).filter_by(id=id).all()
    if(not exists):
        try:
            db_session.add(newUser)
            db_session.commit()
            
        except Exception:
            print(Exception)

def insertRecomendation(db_session, rec):
    db_session.add(rec)
    db_session.commit()



def getConnection():
# connect to the PostgreSQL server
    engine = create_engine(getCredentials())
    #Base.metadata.drop_all(engine)
    #Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    #insertFilms(db_session)

    return db_session
    #r=db_session.query(Film).filter(Film.genre.ilike('Action%')).all()    
    #print("filter_by:", r.)
    #print(db_session.query(Film))

getConnection()

