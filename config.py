import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin<admin@autofix.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	"""docstring for DevelopmentConfig"""
	DEBUG = True
	MAIL_SERVER = 'smtp.google.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
									'mysql+pymysql://ggyy:samsung@192.168.1.240/flask'

class TestingConfig(Config):
	"""docstring for DevelopmentConfig"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
									'mysql+pymysql://ggyy:samsung@192.168.1.240/flask'

class ProductionConfig(Config):
	"""docstring for DevelopmentConfig"""
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
									'mysql+pymysql://ggyy:samsung@192.168.1.240/flask'

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}