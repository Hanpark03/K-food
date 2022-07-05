#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_cors import CORS
from swagger_server.controllers.database_controller import mongodb


def main():

    MONGO_HOST = 'database'     
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.config['MONGODB_SETTINGS'] = {
        'db': 'kfood',
        'host': MONGO_HOST,
        'port': 27017
    }

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Recommandation'}, pythonic_params=True)
    CORS(app.app)
    mongodb.init_app(app.app)   
    app.run(port=8080)


if __name__ == '__main__':
    main()
