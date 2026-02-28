#!/usr/bin/python3
"""changes the name of a State object from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(State).filter\
        (State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
