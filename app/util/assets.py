from flask_assets import Bundle, Environment
from flask import current_app as app

bundles = {
  'root_js': Bundle(
    'js/lib/jquery-2.1.1.min.js',
    'js/app.js',
    output='dist/bundle.js'),
  
  'root_css': Bundle(
    'css/lib/reset.css',
    'css/common.css',
    'css/app.css',
    output='dist/styles.css')
}

assets = Environment(app)
assets.register(bundles)
