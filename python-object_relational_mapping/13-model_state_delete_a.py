#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all states containing 'a'
    states_to_delete = session.query(State).filter(
        State.name.contains('a')
    ).all()

    # Iterate and delete each object
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()
    session.close()
