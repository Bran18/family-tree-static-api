import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Primera, Segunda, Tercera
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/prueba', methods=['GET'])
def prueba():
    # get all the people
    users_gen1 = Primera.query.all()
    
    # map the results and your list of people  inside of the all_people variable
    result = list(map(lambda x: x.serialize(), users_gen1))

    return jsonify(result), 200 

@app.route('/all', methods=['GET'])
def get_all():
    # get all the people
    users_gen1 = Primera.query.all()
    users_gen2 = Segunda.query.all()
    users_gen3 = Tercera.query.all()
    user_all = users_gen1 + users_gen2 + users_gen3
    # map the results and your list of people  inside of the all_people variable
    result = list(map(lambda x: x.serialize(), user_all))

    return jsonify(result), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member_by_id(id):
    # get all the people
    item = Primera.query.get(id)
    if item is None:
        raise APIException('Member not found', status_code=404)

    return jsonify(item.serialize()), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)