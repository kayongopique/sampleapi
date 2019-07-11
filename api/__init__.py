import os
from instance import create_app

app = create_app(config_name= os.getenv('CONFIG') or 'development')

from api.views.auth import appblueprint
from api.views.workerOrders import appblueprint

app.register_blueprint(appblueprint, url_prefix = '/api/')
