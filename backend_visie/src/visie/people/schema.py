from marshmallow import Schema, fields, post_load
from visie.utils.cpf_validator import ValidateCPF


class Person(Schema):
    id_pessoa = fields.Int()
    nome = fields.Str()
    cpf = fields.Str()
    rg = fields.Str()
    data_admissao = fields.Date()
    data_nascimento = fields.Date()
    funcao = fields.Str()


class PersonPaginated(Schema):
    data = fields.Nested(Person, many=True)
    total = fields.Int()
    offset = fields.Int()
    count = fields.Int()


class RegisterPerson(Schema):
    nome = fields.Str()
    cpf = fields.String(validate=ValidateCPF)
    rg = fields.Str()
    data_nascimento = fields.Date('%Y-%m-%d')
    funcao = fields.Str(default=None)

    @post_load
    def check_funcao(self, data, **kwargs):
        if not data['funcao']:
            data['funcao'] = None

        return data


class UpdatePerson(Schema):
    nome = fields.Str()
    cpf = fields.Str()
    rg = fields.Str()
    funcao = fields.Str(allow_none=True)

    @post_load
    def check_funcao(self, data, **kwargs):
        if not data['funcao']:
            data['funcao'] = None

        return data
