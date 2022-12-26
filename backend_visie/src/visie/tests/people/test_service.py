import datetime
from unittest.mock import MagicMock

import pytest
from faker import Faker

from exception import RepositoryException, DataNotFoundException
from visie.people.service import PeopleService

fake = Faker('pt_BR')


@pytest.fixture
def person_service():
    return PeopleService(people_repository=MagicMock())

@pytest.fixture
def person_response():
    return {
        "nome": "gustavo",
        "cpf": "468.852.620-21",
        "rg": "40.443.993-7",
        "data_nascimento": datetime.date.today(),
        "data_admissao": datetime.date.today(),
        "funcao": None
    }


@pytest.fixture
def create_person_payload():
    return {
        "nome": "gustavo",
        "cpf": "468.852.620-21",
        "rg": "40.443.993-7",
        "data_nascimento": "20-12-2022"
    }


def test_create_person(person_service, create_person_payload, person_response):
    person_service.people_repository.check_if_cpf_already_registered.return_value = None
    person_service.people_repository.create.return_value = person_response

    response = person_service.create_person(person_data=create_person_payload)

    assert 'nome' in response
    assert 'rg' in response
    assert 'cpf' in response
    assert 'data_nascimento' in response
    assert 'data_admissao' in response
    assert 'funcao' in response


def test_create_person_with_cpf_already_registered(person_service, create_person_payload):
    exception_msg = 'That cpf is already registered'
    person_service.people_repository.check_if_cpf_already_registered.side_effect = \
        RepositoryException(exception_msg)
    person_service.people_repository.create.return_value = person_response

    with pytest.raises(RepositoryException) as exc_info:
        person_service.create_person(person_data=create_person_payload)

    assert str(exc_info.value) == exception_msg


def test_get_person_does_not_found(person_service):
    exception_msg = 'Person with id [1] does not found.'
    person_service.people_repository.filter_by.return_value = None

    with pytest.raises(DataNotFoundException) as exc_info:
        person_service.get_person(person_id=1)

    assert str(exc_info.value) == exception_msg


def test_get_person(person_service, person_response):
    person_service.people_repository.filter_by.return_value = person_response
    response = person_service.get_person(person_id=2)

    assert 'nome' in response
    assert 'rg' in response
    assert 'cpf' in response
    assert 'data_nascimento' in response
    assert 'data_admissao' in response
    assert 'funcao' in response


def test_update_person_does_not_exist(person_service):
    exception_msg = 'Person with id [1] does not found.'
    person_service.people_repository.filter_by.return_value = None

    with pytest.raises(DataNotFoundException) as exc_info:
        person_service.update_person(person_id=1, data_person_update={'nome': 'test'})

    assert str(exc_info.value) == exception_msg


def test_delete_person_does_not_exist(person_service):
    exception_msg = 'Person with id [1] does not found.'
    person_service.people_repository.filter_by.return_value = None

    with pytest.raises(DataNotFoundException) as exc_info:
        person_service.delete_person(person_id=1)

    assert str(exc_info.value) == exception_msg
