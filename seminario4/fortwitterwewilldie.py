#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Grupo37'
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
import totwitter
import twitter
import io
import json

app = Flask(__name__)
GoogleMaps(app)

searchkey = '#OjalaUnDiezEnSD' #tema a buscar
							   #lo separamos puesto que tambien nos servira para el render_template

twitter_api = totwitter.oauth.login() #autentificacion API twitter
search_results = twitter_api.search.tweets(q = searchkey , count = 100, geocode = '36.516667,-6.283333,800km')
#guardamos el tema a buscar, un contador que nos almacenara 100 tweets, la geolocalizacion de Cadiz (en un campo de 800km)
totwitter.save_json('tweetlist',search_results)#guardamos los resultados en un json

statuslist = totwitter.load_json('tweetlist.json')#carga del json

coordtable = [] #lista de coordenadas

for status in statuslist["statuses"]: #seleccionamos una lista de statuses dentro del json y la recorremos
	if status["geo"]: #si uno de ellos tiene el campo geo activado (con coordenadas geograficas) guardamos sus coordenadas en la tabla
		coordinate = status["coordinates"]
		pos_geo = [coordinate.values()[1][1], coordinate.values()[1][0]]

		coordtable += pos_geo

@app.route("/") #Si no se especifica, te marca la ESI
def mapview2():
	mymap = Map(
		identifier = "view-side",
		lat = 36.516667,
		lng = -6.283333,
		markers = [(36.5380368,-6.2021241)],
		style = "height:800px;width:500px;margin:0;"
	)
	return render_template('template.html', mymap=mymap)

@app.route("/<searchkey>") #al especificar searchkey te saltan los marcadores guardados en la tabla
def mapview():
	mymap = Map(
		identifier = "view-side",
		lat = 36.516667,
		lng = -6.283333,
		markers = coordtable,
		style = "height:800px;width:500px;margin:0;"
	)
	return render_template('template.html', searchkey = searchkey, mymap=mymap)

if __name__ == "__main__":
	app.run(debug=True)