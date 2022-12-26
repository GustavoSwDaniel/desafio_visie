import datetime
from unittest.mock import MagicMock, patch

import pytest

from visie.people.service import PeopleService


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
def person_response_paginate(person_response):
    return{
        "data": [person_response, person_response, person_response],
        "total": 3,
        "offset": 0
    }


@pytest.fixture
def create_person_payload():
    return {
        "nome": "gustavo",
        "cpf": "468.852.620-21",
        "rg": "40.443.993-7",
        "data_nascimento": "20-12-2022"
    }


def test_create_person(client, person_response, create_person_payload):
    with patch.object(PeopleService, 'create_person', return_value=person_response):
        response = client.post('/person', json=create_person_payload)

        response_json = response.json

        assert 'nome' in response_json
        assert 'rg' in response_json
        assert 'cpf' in response_json
        assert 'data_nascimento' in response_json
        assert 'data_admissao' in response_json
        assert 'funcao' in response_json


def test_get_person(client, person_response, create_person_payload):
    with patch.object(PeopleService, 'get_person', return_value=person_response):
        response = client.get('/person/1')

        response_json = response.json

        assert 'nome' in response_json
        assert 'rg' in response_json
        assert 'cpf' in response_json
        assert 'data_nascimento' in response_json
        assert 'data_admissao' in response_json
        assert 'funcao' in response_json


def test_get_people(client, person_response_paginate, create_person_payload):
    with patch.object(PeopleService, 'get_people', return_value=person_response_paginate):
        response = client.get('/people')

        response_json = response.json

        assert len(response_json['data']) == len(person_response_paginate['data'])
        assert 'data' in response_json
        assert 'total' in response_json
        assert 'offset' in response_json


def test_update_person(client, person_response_paginate, create_person_payload):
    payload_update = {'nome': 'test'}

    with patch.object(PeopleService, 'update_person', return_value=None):
        response = client.patch('/person/1', json=payload_update)

        assert response.status_code == 204


def test_delete_person(client, person_response_paginate, create_person_payload):
    with patch.object(PeopleService, 'delete_person', return_value=None):
        response = client.delete('/person/1')

        assert response.status_code == 204
