import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'dummy_secret_key'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	MAIL_SUBJECT_PREFIX = 'Socialite'
	MAIL_SENDER = 'Socialite Team <team.socialite.app@gmail.com>'
	ADMIN = 'delita.makanda@gmail.com',
	POSTS_PER_PAGE = 10
	FOLLOWERS_PER_PAGE = 20
	COMMENTS_PER_PAGE = 10
	SLOW_DB_QUERY_TIME = 0.5
	SQLALCHEMY_RECORD_QUERIES = True


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	"""docstring for DevelopmentConfig."""
	DEBUG = True

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig
}
