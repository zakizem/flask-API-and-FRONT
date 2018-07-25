#coding=utf-8
from flask import Flask, render_template, request, jsonify, make_response
import pyorient, yaml, graphene, json, io

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "root")
client.db_open("testdb", "root", "root")

def SauvgarderDoc(data, classe):
    insererBDD(json.dumps(data), 'Personne')

def insererBDD(data, classe):
    # client.command('CREATE CLASS Personne')
    client.command('INSERT INTO '+classe+' CONTENT '+data)

def updateOLD(classe, requestform):
    resultat=chercherBDD(classe,'email', requestform['email'])    # optionnel ? le temps venu, un truc avec la session
    if len(resultat) > 0:
        updateBDD(classe, json.dumps(requestform), requestform['email'])
        resultat2=chercherBDD(classe,'email', requestform['email'])
        return resultat2
    return('Erreur avec le mail, il ne fallait pas le modifier (le temps venu aussi, il faudra le rendre disabled="disabled" ou un truc du genre)')

def update(classe, data, email):
    updateBDD(classe, data, email)

def updateBDD(classe, data, email):
    # client.command("UPDATE "+classe+' MERGE '+data+" WHERE email='"+email+"'")
    client.command("UPDATE {classe} MERGE {data} WHERE email='{email}'".format(classe=classe, data=data, email=email))

def chercherCategorie(classe, nomAttribut, valeurAttribut, categorie):  ## Retourne la première occurence
    data = client.query("SELECT "+categorie+" FROM "+classe+" "                   ## VOIR DANS QUERIES COMMENT MANIPULER LES JSON ET CLéS
                    "WHERE "+nomAttribut+" = '"+valeurAttribut+"'")
    # print('data cherchée : ')
    # print(data)
    if data==[]:
        return []
    return data[0].oRecordData

def chercherBDD(classe, nomAttribut, valeurAttribut):  ## Retourne la première occurence
    data = client.query("SELECT FROM "+classe+" "
                    "WHERE "+nomAttribut+" = '"+valeurAttribut+"'")
    # print('data cherchée : ')
    # print(data)
    if data==[]:
        return []
    return data[0].oRecordData

def chercherBDD_toutesOccurences(classe, nomAttribut, valeurAttribut):  ## Retourne toutes occurences (format d'OrientDB)
    data = client.query("SELECT FROM "+classe+" "
                    "WHERE "+nomAttribut+" = '"+valeurAttribut+"'")
    return data

def chercherBDDmultiple(classe, requete):
    txt = ''
    for attribut in requete:
        txt = txt + attribut +'='+"'"+requete[attribut]+"'"+' and '
    txt = txt +'true'

    print('txt : '+txt)

    data = client.query("SELECT FROM "+classe+" "
                    "WHERE "+txt)
    return data



#############



def connexionBDD(classe):
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect("root", "root")

    # client.command('INSERT INTO Employee CONTENT {name : 'Jay', surname : 'Miner',
    #     gender : 'M'}')


    # for key in data.items():
    #     print("key : "+key+" - Value : ")
    #     if list == type(data[key]):
    #         print ('ceest une liste')
    #     else:
    #         print(data[key])      # non utilisée, pour l'instant ?                      # non utilisée

#BBD Graphique essais
# @model.route('/graphOrient')   # Deprecated
# def graphOrient():
#     # Connection BDD
#     graph = Graph(Config.from_url('plocal://localhost:2424/testdb','root','root',initial_drop = False))
#
#     # Initialize Registries
#     Node = declarative.declarative_node()
#     Relationship = declarative.declarative_relationship()
#
#     # Create Vertex Class
#     class Person(Node):
#        element_plural = 'persons'
#        name = String()
#        zone = String()
#        def __init__(self):
#            self.name = ""
#            self.zone = ""
#
#     # Create Edge Class
#     class Likes(Relationship):
#        pass
#
#     # # Initialize Schema
#     # graph.create_all(Node.registry)
#     # graph.create_all(Relationship.registry)
#
#     # Bind Schema
#     graph.include(Node.registry)
#     graph.include(Relationship.registry)
#
#
#     # Person.objects.create(
#     # name = 'lightSensor',
#     # zone = 'kitchen')
#
#     # graph.Persons.create(
#     # name = 'smokeAlarm',
#     # zone = 'kitchen')
#
#     return ("fait")
#
# @model.route('/orient')       # Deprecated ?
# def orient():
#     client = pyorient.OrientDB("localhost", 2424)
#     print('1')
#     session_id = client.connect("root", "root")
#     print (client.db_list())
#
#     return (client.db_list())
