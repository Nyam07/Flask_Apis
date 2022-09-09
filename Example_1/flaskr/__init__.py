from flask import Flask, jsonify
from models import setup_db, Plant
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')

        return response

    @app.route('/plants')
    def get_plants():
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]


        return jsonify({
            "success": True,
            "plants":formatted_plants,
        })

    @app.route('/')
    def home():
        data = [
            {
                "name": "Oleander",
                "scientific_name": "Nerium oleander",
                "is_poisonous": True,
                "primary_color": "pink"
            },

            {
                "name": "Water Hemlock",
                "scientific_name": "Cicuta",
                "is_poisonous": True,
                "primary_color": "white"
            },

            {
                "name": "Bamboo",
                "scientific_name": "Bamboosa aridinarifolia",
                "is_poisonous": False,
                "primary_color": "green"
            },

            {
                "name": "Carrot",
                "scientific_name": "Daucas carota",
                "is_poisonous": False,
                "primary_color": "orange"
            },

            {
                "name": "Lemon",
                "scientific_name": "Citrus limonium",
                "is_poisonous": False,
                "primary_color": "yellow"
            },
             {
                "name": "Foxglove",
                "scientific_name": "Digitalis",
                "is_poisonous": True,
                "primary_color": "purple"
            },
             {
                "name": "Lily of the Valley",
                "scientific_name": "Convallaria majalis",
                "is_poisonous": True,
                "primary_color": "white"
            },
            {
                "name": "Dieffenbachia",
                "scientific_name": "Dieffenbachia seguine",
                "is_poisonous": True,
                "primary_color": "green"
            },
            {
                "name": "Tomato",
                "scientific_name": "Lycopersican esculentum",
                "is_poisonous": False,
                "primary_color": "red"
            },
             {
                "name": "Spinach",
                "scientific_name": "Lactuca sativa",
                "is_poisonous": False,
                "primary_color": "green"
            },

            {
                "name": "Orange",
                "scientific_name": "Citrus aurantium",
                "is_poisonous": False,
                "primary_color": "orange"
            }
        ]

        for item in data:
            plant = Plant(item['name'], item['scientific_name'], item['is_poisonous'], item['primary_color'])

            plant.insert()

        return jsonify({
            "Success":True
        })
    
    return app