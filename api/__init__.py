import os
from instance import create_app
from flask_cors import CORS

cors =CORS()

app = create_app(config_name= os.getenv('CONFIG') or 'development')

cors.init_app(app)

from api.views.auth import authblueprint
from api.views.workerOrders import appblueprint

origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
cors.init_app(appblueprint, origins=origins)
cors.init_app(authblueprint, origins=origins)

app.register_blueprint(appblueprint, url_prefix = '/api/')
app.register_blueprint(authblueprint, url_prefix = '/api/')

