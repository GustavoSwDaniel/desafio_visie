import re

from marshmallow import ValidationError


class ValidateCPF:
    def __init__(self, cpf):
        self.cpf = cpf
        self.validate_cpf()

    def validate_cpf(self):
        if not self.cpf:
            return False

        new_cpf = self.__calc_digit(self.cpf[:9])
        new_cpf = self.__calc_digit(new_cpf)

        if new_cpf == self.cpf:
            return True
        raise ValidationError("Invalid CPF")

    @staticmethod
    def __calc_digit(cpf):
        if not cpf:
            return False

        sequence = cpf[0] * len(cpf)

        if sequence == cpf:
            return False
        soma = 0
        for key, multiplier in enumerate(range(len(cpf) + 1, 1, -1)):
            soma += int(cpf[key]) * multiplier

        rest = 11 - (soma % 11)
        rest = rest if rest <= 9 else 0
        return cpf + str(rest)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self._clear_cpf(cpf)

    @staticmethod
    def _clear_cpf(cpf):
        return re.sub("[^0-9]", "", cpf)