import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MAetapAEjDx8S2wmbEgKKVTCVZFgx6eupExY4CxZ'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app','db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False