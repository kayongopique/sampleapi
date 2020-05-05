from instance import create_app

app = create_app(config_name='testing')

from api.views import appblueprint, authblueprint

app.register_blueprint(appblueprint, url_prefix = '/api/')
app.register_blueprint(authblueprint, url_prefix = '/api/')
