from sqlalchemy import Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class Resource(Base):
    __tablename__ = "resource"
    id = Column(String(20), primary_key=True)
    name = Column(String(100))
    created = Column(DateTime())

    def update(self, id=None, name=None, created=None):
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created

    def dump(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}


def init_db(uri):
    engine = create_engine(uri)
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
