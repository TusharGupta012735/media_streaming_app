from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Url Format : postgresql://<username>:<password>@<host>:<port>/<database_name> 
DATABASE_URL = "postgresql://postgres:TusharGupta%402005@localhost:5432/audio_streaming_app"

engine = create_engine(DATABASE_URL) #central source of connection to database, tells what and whereaouts of database to app
sessionLocal = sessionmaker( #manage interaction with db
    # autocommit = False, depricated
    autoflush=False, #stops session from flushing db changes automatically before a new request
    bind=engine,
) 
#a factory to create session to interact with database
def get_db():
    db = sessionLocal() #create a session instance to actually interact with database
    try :
        yield db
    finally :
        db.close()