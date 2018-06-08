#coding=utf-8
from flask import Flask, render_template, request, jsonify, make_response, session
import pyorient, yaml, graphene, json, io
from appli.model import *

from flask import Blueprint

traitementExceptions = Blueprint('traitementExceptions', __name__)

@traitementExceptions.errorhandler(404)   # ne marche pas
def page_not_found(e):
    return("ERREUR 400000000000000004 !!!!")


@traitementExceptions.route('/ola', methods=['GET', 'POST'])
def ola():
    return('olaaa')


if __name__ == "__main__":
    print (__name__)
    traitementExceptions.run()
