from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_flatpages import FlatPages
from flask_caching import Cache
from flask_sitemap import Sitemap
from config import config

mail = Mail()
moment = Moment()
pagedown = PageDown()
pages = FlatPages()
db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'simple'})
ext = Sitemap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    assets = Environment(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    mail.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)
    pages.init_app(app)
    cache.init_app(app)
    ext.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .api_1_0 import api as api_1_0_blueprint
    from .api_2_0 import api_v2 as api_2_0_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')
    app.register_blueprint(api_2_0_blueprint, url_prefix='/api/v2.0')

    root_js = Bundle(
        'js/vendors/jquery-2.1.1.min.js',
        'js/app.js',
        output='dist/bundle.js')

    root_css = Bundle(
        'css/vendors/tailwind.min.css',
        'css/app.css',
        output='dist/styles.css')


    assets.register('root_js', root_js)
    assets.register('root_css', root_css)

    return app
