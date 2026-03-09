#!/usr/bin/python3
"""
Prints the State object with the name passed as argument.
Safe from SQL injection.
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

    # Query for the state name passed as the 4th argument
    # SQLAlchemy's filter(State.name == var) is inherently safe
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display ID if found, otherwise "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
