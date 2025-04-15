import random


class Helpers:
    @staticmethod
    def create_email():
        email = f'timofei_vasilev_20_{random.randint(100, 999)}@yandex.ru'
        return email

    @staticmethod
    def create_password():
        password = random.randint(100000, 999999)
        return password