import logging
from asyncio import current_task

from sqlalchemy import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, Session
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:
    def __init__(self, database_url: str) -> None:
        self.__engine = create_engine(database_url, echo=False, pool_size=5, max_overflow=10)
        self.__session_factory = scoped_session(orm.sessionmaker(self.__engine, expire_on_commit=False,
                                                                 class_=Session))

    def create_database(self) -> None:
        Base.metadata.create_all(self.__engine)

    @contextmanager
    def session(self) -> Session:
        session: Session = self.__session_factory()
        try:
            yield session
        except Exception:
            logger.exception('Postgres Session rollback because of exception')
            session.rollback()
            raise
        finally:
            session.close()
