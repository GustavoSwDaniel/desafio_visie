from flask import request, jsonify

from visie.people import bp
from visie import db
from visie.people import schema as people_schema
from visie.people.repository import PeopleRepository
from visie.people.service import PeopleService


@bp.route('/person', methods=['POST'])
def create_person():
    person = people_schema.RegisterPerson().load(request.json)

    people_repository = PeopleRepository(session_factory=db.session)
    people_service = PeopleService(people_repository=people_repository)

    response = people_service.create_person(person_data=person)
    return jsonify(people_schema.Person().dump(response)), 201


@bp.route('/people', methods=['GET'])
def get_people():
    params = {
        'limit': int(request.args.get('limit', 10)),
        'offset': int(request.args.get('offset', 0))
    }

    people_repository = PeopleRepository(session_factory=db.session)
    people_service = PeopleService(people_repository=people_repository)
    response = people_service.get_people(params=params)
    return jsonify(people_schema.PersonPaginated().dump(response)), 200


@bp.route('/person/<int:person_id>', methods=['GET'])
def get_person(person_id: int):
    people_repository = PeopleRepository(session_factory=db.session)
    people_service = PeopleService(people_repository=people_repository)

    person = people_service.get_person(person_id=person_id)
    return jsonify(people_schema.Person().dump(person)), 200


@bp.route('/person/<int:person_id>', methods=['PATCH'])
def update_person(person_id):
    person_data_update = people_schema.UpdatePerson().load(request.json)

    people_repository = PeopleRepository(session_factory=db.session)
    people_service = PeopleService(people_repository=people_repository)

    people_service.update_person(person_id=person_id, data_person_update=person_data_update)
    return {}, 204


@bp.route('/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id: int):
    people_repository = PeopleRepository(session_factory=db.session)
    people_service = PeopleService(people_repository=people_repository)

    people_service.delete_person(person_id=person_id)
    return {}, 204
