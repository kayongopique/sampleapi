from instance import create_app

app = create_app(config_name='testing')

from api.views import appblueprint

app.register_blueprint(appblueprint, url_prefix = '/api/')
