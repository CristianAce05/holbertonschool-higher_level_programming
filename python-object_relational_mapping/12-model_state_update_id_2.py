#!/usr/bin/python3
"""
Updates the name of a State object from the database hbtn_0e_6_usa.
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

    # Query for the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name attribute if the object exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
