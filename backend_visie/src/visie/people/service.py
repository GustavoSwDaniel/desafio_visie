import datetime
from typing import Dict, List

from src.exception import DataNotFoundException
from src.visie.people.repository import PeopleRepository
from src.visie.people.models import People
from src.visie.utils.paginate import paginate


class PeopleService:
    def __init__(self, people_repository: PeopleRepository):
        self.people_repository = people_repository

    def get_people(self, params: Dict) -> Dict:
        people, total = self.people_repository.get_all_paginated(params=params)
        return paginate(result=people, offset=params.get('offset'), total=total)

    def get_person(self, person_id: int) -> People:
        response = self.people_repository.filter_by({'id_pessoa': person_id})

        if not response:
            raise DataNotFoundException(f'Person with id [{person_id}] does not found.')

        return response

    def __check_cpf_already_registered(self, cpf: str) -> None:
        self.people_repository.check_if_cpf_already_registered(cpf=cpf)

    def create_person(self, person_data: Dict) -> People:
        self.__check_cpf_already_registered(cpf=person_data.get('cpf'))

        response = self.people_repository.create(person_data)
        return response

    def update_person(self, person_id: int, data_person_update: Dict) -> None:
        self.get_person(person_id=person_id)

        self.people_repository.update_by_person_id(pk=person_id, values=data_person_update)

    def delete_person(self, person_id: int) -> None:
        person = self.get_person(person_id=person_id)
        self.people_repository.delete(person)
