import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = 'balancedmarketplacelove'

SQLALCHEMY_DATABASE_URI = 'postgresql://marketplace:coolkicksman@127.0.0.1/marketplace'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

DEBUG = True
BALANCED_MARKETPLACE_URI = '/v1/marketplaces/TEST-MP3JI8LVVKbCud35kuWNa3QI'
BALANCED_API_KEY = '7aad003e041011e3ab2b026ba7d31e6f'
