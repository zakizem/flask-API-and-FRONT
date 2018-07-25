from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

# from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

# api = Api(app)

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_SESSION_COOKIE'] = True

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=3)

app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/'

app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_SECRET_KEY'] = 'clé super secrète man'
jwt = JWTManager(app)


# ##### API avec flask_restful
#
# class InsertionReponses(Resource):
#     decorators = [jwt_required]
#     def post(self):
#         return 'data'
#
# class Refresh(Resource):
#     decorators = [jwt_refresh_token_required]
#     def get(self):
#         # Create the new access token
#         current_user = get_jwt_identity()
#         access_token = create_access_token(identity=current_user)
#
#         # Set the JWT access cookie in the response
#         resp = jsonify({'refresh': True})
#         set_access_cookies(resp, access_token)
#
#         resp.status_code = 200
#         return resp
#
# api.add_resource(InsertionReponses, '/sendRequest')
# api.add_resource(Refresh, '/token/refresh')
#
# ##### FIN API

@app.route('/vide', methods=['POST'])
@jwt_required
def vide():
    data=request.get_json()
    return jsonify({'vide': True,'iii': data})

@app.route('/getTokens', methods=['POST'])
def a():
    access_token = create_access_token(identity='blablue')
    refresh_token = create_refresh_token(identity='blablue')
    resp = jsonify({'login': True,'data': 'bla'})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    print (__name__)
    app.run(host="127.0.0.1", port=8011, threaded=True)
