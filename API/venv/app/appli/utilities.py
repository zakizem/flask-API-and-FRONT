#coding=utf-8
from flask import Flask, render_template, request, jsonify, make_response, session, redirect, flash
import pyorient, yaml, graphene, json, io
from appli.model import *
from functools import wraps

def Existe(attribut ,valeur):
    resultat=chercherBDD('Personne', attribut, valeur)
    if resultat!=[]:
        return True
    return False

def authentification(data):
    if all (k in data for k in ("email","password")):
        if Existe('email' ,data['email']):
            if Existe('password' ,data['password']):
                return 'authentification réussie'
            else:
                return 'Mauvais mot de passe'
        return "L'adresse mail n'existe pas"
    return "Merci de remplir les champs"

######### avant API :

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'session_valide' in session:  #and session['session_valide']:
            flash("Accès autorisé")
            return f(*args, **kwargs)
        else:
            flash("Vous avez besoin de vous authentifier")
            return redirect ('/')
    return wrap

def validation_identifiants(email, password):
    resultat=chercherBDD('Personne','email', email)
    if len(resultat) > 0:
        if resultat[0].oRecordData['password'] == password:
            return resultat[0].oRecordData
        return('Mot de passe non valide')
    return('Email non trouvé')

def setSession(resultat_validation):
    session['prenom']=resultat_validation['prenom']
    session['nom']=resultat_validation['nom']
    session['email']=resultat_validation['email']
    session['password']=resultat_validation['password']
    session['session_valide']=True
    # session['tout']=resultat_validation

def session_validation():
    if 'email' in session and 'password' in session and 'prenom' in session:
        resultat_validation=validation_identifiants(session['email'], session['password'])
        if type(resultat_validation) != str:
            session['session_valide']=True
            return resultat_validation
    return ("pas de session")

def return_form():
    return render_template("formulaire.html", formulaire=lireDuFichier('formulaire_config_questions.yaml'), prerempli=prerempli, update='' )
    # FAUT GERER LE UPDATE, SINON CE N'EST PAS LA PEINE     # A VOIR

def est_un_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def ecrireDansFichier(data,fichier):
    with io.open(fichier, 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

def lireDuFichier(fichier):
    with open(fichier, 'r') as stream:
        data_loaded = yaml.load(stream)

    print ("Nom des questions unique dans le formulaire ? ")
    print(nomUniqueFormulaire(data_loaded))

    return data_loaded

def nomUniqueFormulaire(data):
    for id_1, element_1 in enumerate(data):
        for id_2, element_2 in enumerate(data):
            if id_1 != id_2:
                if element_1['nom_de_la_question'] == element_2['nom_de_la_question']:
                    return False
    return True         # Voir comment traiter les exceptions ?

def conversionLisibleJinja(data):
    return yaml.load(yaml.dump(data))      # ou : parcourir le requestData avec for in de python, tout mettre en String, puis convertir en Json

def nettoyerData(data):
    for element in data:
        if '' == data[element]:
            del data[element]
    return data                   # non utilisée
