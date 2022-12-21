import os


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'mariadb+mariadbconnector://gustavodaniel:Z3VzdGF2b2Rh@jobs.visie.com.br:3306/gustavodaniel')