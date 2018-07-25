from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

from appli.utilities import *
from appli.model import *
from appli.form import *
from appli.traitementExceptions import *

from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

api = Api(app)

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

##### API avec flask_restful

class QuestionsCategorie(Resource):
    def get(self, categorie):
        data= lireDuFichier('formulaire_config_questions.yaml')

        etapes = []
        for key in data:
            etapes.append(key)

        if categorie in data:
            print(data[categorie])
            return jsonify(data[categorie])
        return 'categorie inexistante', 404

class questionsNext(Resource):
    def get(self, categorieCourante):
        data= lireDuFichier('formulaire_config_questions.yaml')
        i = 0
        for key in data:
            if i == 1:
                return jsonify({ 'etapeCourante' : key, 'data' : data[key]})
            elif key == categorieCourante:
                i=i+1
        return 'erreur', 404

class QuestionsPrecedentes(Resource):
    def get(self, categorieCourante):
        data= lireDuFichier('formulaire_config_questions.yaml')
        avant = ''
        for key in data:
            if key == categorieCourante:
                if avant != '':
                    return jsonify({ 'etapeCourante' : avant, 'data' : data[avant]})
            avant = key
        return 'erreur', 404

class InsertionReponses(Resource):
    decorators = [jwt_required]
    def post(self):
        data=request.get_json(force=True)
        current_user = get_jwt_identity()
        print('current user : ')
        print(current_user)

        if Existe('email',current_user):   #Enlever ça pour le update et mettre un décorateur ??
            # return 'Le mail existe déja'     # Ajouter status
            update('Personne',data, current_user)
            return 'contenu mis à jour', 200

        return 'Adresse mail '+current_user+' n existe pas', 400

        # SauvgarderDoc(data, 'Personne')
        # resultat=chercherBDD('Personne','email', data['email'])
        # return resultat

class Signup(Resource):
    def post(self):
        data=request.get_json()
        return signup(data)

class Authentification(Resource):
    def post(self):
        data = request.get_json()
        auth = authentification(data)
        if auth == 'authentification réussie':
            # Creation des tokens
            access_token = create_access_token(identity=data['email'])
            refresh_token = create_refresh_token(identity=data['email'])

            infos=chercherBDD('Personne','email',data['email'])

            # Set the JWT cookies in the response
            resp = jsonify({'login': True,'data': infos})
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            resp.status_code = 200
            return resp
        rv = make_response(jsonify(auth), 401)
        rv.set_cookie('Un Cookie', 'I am cookie', secure=False, path='/', httponly=False)
        return rv

class Protected(Resource):
    decorators = [jwt_required]
    def get(self):
        d=jsonify({'message' : 'Contenu protégé accessible'})
        return d
        # username = get_jwt_identity()
        # return jsonify({'hello': 'from {}'.format(username)}), 200

class Refresh(Resource):
    decorators = [jwt_refresh_token_required]
    def get(self):
        # Create the new access token
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        # Set the JWT access cookie in the response
        resp = jsonify({'refresh': True})
        set_access_cookies(resp, access_token)

        resp.status_code = 200
        return resp

class Logout(Resource):
    def post(self):
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        resp.status_code = 200
        return resp

api.add_resource(InsertionReponses, '/envoiReponses')
api.add_resource(Authentification, '/authentification')
api.add_resource(Protected, '/protected')
api.add_resource(Signup, '/signup')

api.add_resource(Refresh, '/token/refresh')
api.add_resource(Logout, '/token/logout')

api.add_resource(QuestionsCategorie, '/questionsCategorie/<string:categorie>', endpoint = 'QuestionsCategorie')
api.add_resource(questionsNext, '/questionsCategorieSuivante/<string:categorieCourante>', endpoint = 'questionsNext')
api.add_resource(QuestionsPrecedentes, '/questionsCategoriePrecedente/<string:categorieCourante>', endpoint = 'QuestionsPrecedentes')

##### FIN API

@app.route('/vide', methods=['POST'])
@jwt_required
def vide():
    current_user = get_jwt_identity()
    data=request.get_json()
    return jsonify({'vide': True,'iii': data, 'identité': current_user})

@app.route('/a', methods=['POST'])
def a():
    access_token = create_access_token(identity='blablue')
    refresh_token = create_refresh_token(identity='blablue')
    resp = jsonify({'login': True,'data': 'bla'})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    resp.status_code = 200
    return resp

@app.route('/')
def index():
    #return ('API en marche..')
    # return json.dumps(app.config)
    data=chercherCategorie('Personne', 'email', 'ola', 'identite')
    print('resultat recherche catég : ')
    print(data)

    data= lireDuFichier('formulaire_config_questions.yaml')
    print('TYPE resultat recherche identite: ')
    print(type(data['identite']))

    str = ''
    for key in data:
        str = str + ' ' + key

    return jsonify(str)

    return render_template("vueJS/index.html")


if __name__ == "__main__":
    print (__name__)
    app.run(host="127.0.0.1", port=8011, threaded=True)
