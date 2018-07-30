# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf8')
import snips_nlu

snips_nlu.load_resources("es")

import io
import json
from snips_nlu import SnipsNLUEngine, load_resources


with io.open("trained.json") as f:
    engine_dict = json.load(f)

engine = SnipsNLUEngine.from_dict(engine_dict)

#phrase = raw_input("Pregunta: ")


def pregunta(phrase):
    r = engine.parse(unicode(phrase))
    return json.dumps(r, indent=2)
    #print(json.dumps(r, indent=2))



from SPARQLWrapper import SPARQLWrapper, JSON


def consulta_formula1(formula1):

    sparql = SPARQLWrapper("http://localhost:8890/sparql/AutomovilismoNuevo")
    sparql.setQuery("""
                select distinct ?Nombre where {
                    ?Pilotos skos:narrower skos:PilotosF1 .
                    ?Pilotos rdfs:label ?Nombre .
                    }
                    """)
    # definition
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    print(results)
    datos = []
    #datos1 = []
    for result in results["results"]["bindings"]:
        datos.append(result["Nombre"]["value"])
        #datos1.append(datos.split("example:")) #limpio el example:
    print("estos son los datos")
    #print(datos)
    return datos

def consulta_EquiposF1(equiposf1):

    sparql1 = SPARQLWrapper("http://localhost:8890/sparql/AutomovilismoNuevo")
    sparql1.setQuery("""
                select distinct ?Nombre where {
                    ?EquiposF1 skos:narrower skos:NombreEquiposF1 .
                    ?EquiposF1 rdfs:label ?Nombre .
                    }
                    """)
    # definition
    sparql1.setReturnFormat(JSON)
    results1 = sparql1.query().convert()

    print(results1)
    datos1 = []
    #datos1 = []
    for result1 in results1["results"]["bindings"]:
        datos1.append(result1["Nombre"]["value"])
        #datos1.append(datos.split("example:")) #limpio el example:
    print("estos son los datos1")
    #print(datos)
    return datos1   

def consulta_CampeonesF1(campeonesf1):

    sparql2 = SPARQLWrapper("http://localhost:8890/sparql/AutomovilismoNuevo")
    sparql2.setQuery("""
                select distinct ?Nombre where {
                    ?Pilotos skos:related skos:PilotosF1Campeones .
                    ?Pilotos rdfs:label ?Nombre .
                    }
                    """)
    # definition
    sparql2.setReturnFormat(JSON)
    results2 = sparql2.query().convert()

    print(results2)
    datos2 = []
    #datos1 = []
    for result2 in results2["results"]["bindings"]:
        datos2.append(result2["Nombre"]["value"])
        #datos1.append(datos.split("example:")) #limpio el example:
    print("estos son los datos1")
    #print(datos)
    return datos2     

def consulta_Categorias(categorias):

    sparql3 = SPARQLWrapper("http://localhost:8890/sparql/AutomovilismoNuevo")
    sparql3.setQuery("""
                select distinct ?Nombre where {
                    skos:Automovilismo skos:narrower ?categorias .
                    ?categorias skos:prefLabel ?Nombre .
                    }
                    """)
    # definition
    sparql3.setReturnFormat(JSON)
    results3 = sparql3.query().convert()

    print(results3)
    datos3 = []
    #datos1 = []
    for result3 in results3["results"]["bindings"]:
        datos3.append(result3["Nombre"]["value"])
        #datos1.append(datos.split("example:")) #limpio el example:
    print("estos son los datos1")
    #print(datos)
    return datos3    

def consulta_teamF1(teamF1):

    sparql4 = SPARQLWrapper("http://localhost:8890/sparql/AutomovilismoNuevo")
    sparql4.setQuery("""
                select distinct ?Nombre where {
                    ?EquiposF1 skos:narrower skos:NombreEquiposF1 .
                    ?EquiposF1 skos:prefLabel ?NomEquiposF1 .
                    ?Pilotos skos:narrower ?EquiposF1 .
                    ?Pilotos rdfs:label ?Nombre .
                    Filter regex(?NomEquiposF1, '"""+teamF1+"""', "i") 
                    }
                    """)
    # definition
    sparql4.setReturnFormat(JSON)
    results4 = sparql4.query().convert()

    print(results4)
    datos4 = []
    #datos1 = []
    for result4 in results4["results"]["bindings"]:
        datos4.append(result4["Nombre"]["value"])
        #datos1.append(datos.split("example:")) #limpio el example:
    print("estos son los datos1")
    #print(datos)
    return datos4         