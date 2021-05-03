import os
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import json
from models import Base, Film


CSV_FILE_PATH = os.getcwd()+'/movie_data.csv'
CONFIG_FILE_PATH = os.getcwd()+'/config.json'

def getCredentials():
    with open(CONFIG_FILE_PATH, "r") as file:
        conf = json.load(file)
    conn_string = conf["DATABASE_URI"]
    return conn_string

def insertInDB(db_session):
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
            plot = i[11]

            newFilm = Film(title,year,link,rating,runtime,genre,plot,0)

            db_session.add(newFilm)
            db_session.commit()
            #print(s.query(Film).first())
conn = None

# connect to the PostgreSQL server
engine = create_engine(getCredentials())
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()
insertInDB(db_session)
#r=db_session.query(Film).filter(Film.genre.ilike('Action%')).all()    
#print("filter_by:", r.)
#print(db_session.query(Film))

