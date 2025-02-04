# Movie Recommendator telegram Conversational Agent

The following repository uses an already existing movie database 
(top 50 IMDB movies based on ratings) and [DialogFlow](https://cloud.google.com/products/conversational-agents)
to create a conversational agent that will recommend movies based on:
1. The genre of the film the user wants
2. The popularity of the film the user wants

  
To interact with the DB the program is using [SQLAlchemy](https://www.sqlalchemy.org/)
python library and is using the Google API to interact with DiaglFlow.
