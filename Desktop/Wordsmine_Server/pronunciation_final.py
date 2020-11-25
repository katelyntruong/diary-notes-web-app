import flask
import requests
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app_id = '911a0028'
app_key = '5cdd6ae1c0b69d9e3113f7a1abc2d199'

language = 'en-gb'

fields = 'pronunciations'
strictMatch = 'false'

@app.route('/api/word/lookup', methods=['GET'])
def api():
	if 'word' in request.args:
		word_id = request.args['word']
		url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
		r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
		if r.status_code != 200:
			return "Error"
	else:
		return "Error"    
	return jsonify(r.json()['results'][0]["lexicalEntries"][0]['entries'][0]['pronunciations'][0]["audioFile"])

@app.route('/api/word', methods=['GET'])
def api_all():
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + 'know' + '?fields=' + fields + '&strictMatch=' + strictMatch
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	return jsonify(r.json())
app.run()