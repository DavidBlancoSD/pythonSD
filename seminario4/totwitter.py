#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Grupo37'
import twitter
import io
import json

#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'EV2drcrnslSTUbmuL0cYG6xQE'
    CONSUMER_SECRET = 'bvlv4YsuP0caCmvYsI7Cw6Fxh11nJKKkQm8HSLGgpOHGLgzhvU'
    OAUTH_TOKEN = '161720260-3VqJpAAzqdSnxmTqgzihm5VGBbGttvw3XRAlf31Y'
    OAUTH_TOKEN_SECRET = 'RWQvycD5JnbWkWozqUlOKA74G4R6MqmdRUKDgHmuPOzQv'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()
