from sqlalchemy import update, select

from visie.infrastructure.repository.base_repository import IRepository
from visie.infrastructure.database.database_sql import Base


class SqlRepository(IRepository):
    model = Base

    def get_all(self):
        with self.session_factory() as session:
            result = session.execute(select(self.model))
            return result.scalars().all()

    def filter_by(self, params):
        with self.session_factory() as session:
            result = session.execute(select(self.model).filter_by(**params))
            return result.scalars().first()

    def filter_all_by(self, params):
        with self.session_factory() as session:
            result = session.execute(select(self.model).filter_by(**params))
            return result.scalars()

    def create(self, values):
        with self.session_factory() as session:
            _model = self.model(**values)
            session.add(_model)
            session.commit()
            return _model

    def update(self, pk, values):
        with self.session_factory() as session:
            session.execute(update(self.model).where(self.model.id == pk).values(**values))
            session.commit()

    def delete(self, _model: Base):
        with self.session_factory() as session:
            session.delete(_model)
            session.commit()

    def commit(self):
        with self.session_factory() as session:
            session.commit()

    def rollback(self):
        with self.session_factory() as session:
            session.rollback()
