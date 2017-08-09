import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	MAIL_SUBJECT_PREFIX = 'socialite app'
	MAIL_SENDER = os.environ.get('MAIL_USERNAME')
	ADMIN = ['delita.makanda@gmail.com']
	POSTS_PER_PAGE = 10
	FOLLOWERS_PER_PAGE = 20
	COMMENTS_PER_PAGE = 10
	SLOW_DB_QUERY_TIME = 0.5
	SSL_DISABLE = False
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_RECORD_QUERIES = True
	MAIL_SERVER = os.environ.get('MAILGUN_SMTP_SERVER')
	MAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAILGUN_SMTP_LOGIN')
	MAIL_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
	FLATPAGES_EXTENSION = '.md'
	FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'headerid']
	ADMINS = ['delita.makanda@gmail.com', 'makanda.delita@orange.fr']


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	"""docstring for DevelopmentConfig."""
	DEBUG = True
	FLATPAGES_AUTO_RELOAD = DEBUG
	MAIL_SERVER = 'smtp.mailgun.org'
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

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)

		import logging
		from logging.handlers import SMTPHandler
		credentials = None
		secure = None
		if getattr(cls, 'MAIL_USERNAME', None) is not None:
			credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
			if getattr(cls, 'MAIL_USE_TLS', None):
				secure = ()
		mail_handler = SMTPHandler(
			mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
			fromaddr=cls.MAIL_SENDER,
			toaddrs=[cls.ADMIN],
			subject=cls.MAIL_SUBJECT_PREFIX + ' Application error',
			credentials=credentials,
			secure=secure)
		mail_handler.setLevel(logging.ERROR)
		app.logger.addHandler(mail_handler)


class HerokuConfig(ProductionConfig):
	SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

	@classmethod
	def init_app(cls, app):
		ProductionConfig.init_app(app)

		import logging
		from logging import StreamHandler
		file_handler = StreamHandler()
		file_handler.setLevel(logging.WARNING)
		app.logger.addHandler(file_handler)

		from werkzeug.contrib.fixers import ProxyFix
		app.wsgi_app = ProxyFix(app.wsgi_app)


class UnixConfig(ProductionConfig):
	@classmethod
	def init_app(cls, app):
		ProductionConfig.init_app(app)

		import logging
		from logging.handlers import SysLogHandler
		syslog_handler = SysLogHandler()
		syslog_handler.setLevel(logging.WARNING)
		app.logger.addHandler(syslog_handler)



config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'heroku': HerokuConfig,
	'unix': UnixConfig,

	'default': DevelopmentConfig
}
