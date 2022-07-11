from flask import Flask
from flask_restful import Api
from src.entry_point.solar_resource import SolarResource
from src.conf import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# solar_type choices are 'planet', 'asteroid'
api.add_resource(SolarResource, '/solar/<string:solar_type>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)