from flask import Flask
from flask_restful import Api
from src.entry_point.solar_resource import SolarResource

app = Flask(__name__)
