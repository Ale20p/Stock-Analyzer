# Used for creating a connection to a database using a specified url.
# The connection is the "engine" that SQLAlchemy uses to execute SQL statements.
from sqlalchemy import create_engine
# It is a factory for creating database session objects.
# A session represents a temporary "workspace" for interacting with the database.
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = "postgresql://postgres:101040asr@localhost:5433/postgres"

# This line creates a database engine that serves as the core interface to the database.
# echo=True: Enables SQL query logging. When set to True, SQLAlchemy outputs all SQL statements it executes to the console, which is useful for debugging.
engine = create_engine(DATABASE_URL, echo=True)
# This line creates a session factory for database interactions.
# autocommit=False: Disables automatic commiting of transactions. Changes to the database are only commited when explicitly called with session.commit() .
# autoflush=False: Prevents automatic flushing of changes to the database. Flushing pushes changes to the database but doesn't commit them. By setting this to False, changes are only flushed when explicitly calling session.flush() or session.commit() .
# bind=engine: Links the session to the database engine created earlier, ensuring that all sessions use the same database connection.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates a new database session.
# Yields this session to be used by the calling code.
# Ensures the session is properly closed after the calling code finishes regarless of success or failure.
def get_db():
    db = SessionLocal()
    try:
        yield db # Passed the db session to the calling code.
    finally:
        db.close()
