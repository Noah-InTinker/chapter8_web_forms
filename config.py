import os


class Config(object):
    """Define app configirations"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'