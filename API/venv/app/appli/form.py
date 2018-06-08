from wtforms import Form, BooleanField, StringField, PasswordField, validators
from appli.utilities import *


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms and conditions', [validators.DataRequired()])


class DynamicForm(Form):
    def __init__(self, Form):
        setattr(self, 'formulaire', lireDuFichier('formulaire_config_questions.yaml'))
        formulaire=lireDuFichier('formulaire_config_questions.yaml')
        for element in formulaire:
            setattr(self, element['nom_de_la_question'], StringField(element['texte'], [validators.Length(min=4, max=25)]))


class MyClasss():
    def __init__(self):
        setattr(self, 'nom', 'ds')
        setattr(self, 'prenom', 'fdsfsd')
