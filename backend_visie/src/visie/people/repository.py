from sqlalchemy import select, update, func

from src.exception import RepositoryException
from src.visie.infrastructure.repository.repository import SqlRepository
from src.visie.people.models import People


class PeopleRepository(SqlRepository):
    model = People

    def get_all_paginated(self, params: dict):
        with self.session_factory() as session:
            results = session.execute(select(self.model).limit(params.get('limit')).offset(params.get('offset')))

            total = session.execute(select([func.count(self.model.id_pessoa)]).select_from(self.model))

            total = total.scalar()
            results = results.scalars().all()

            return results, total

    def check_if_cpf_already_registered(self, cpf: str):
        with self.session_factory() as session:
            result = session.execute(
                select(self.model).
                where(self.model.cpf == cpf)
            )
            if result.scalars().first():
                raise RepositoryException('That cpf is already registered')

    def update_by_person_id(self, pk, values):
        with self.session_factory() as session:
            session.execute(update(self.model).where(self.model.id_pessoa == pk).values(**values))
            session.commit()
