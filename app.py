from flask import Flask, render_template, jsonify, make_response, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl
import re
import json
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/commit_result')
def test():
	with open('data/commit_result.json', 'r',encoding='utf-8') as f:
		info = json.load(f)
	return json.dumps(info,indent='\t',ensure_ascii=False)


@app.route('/commit/api', methods=['GET'])
def commitapi(): 
	with open('data/commit_result.json', 'r',encoding='utf-8') as f:
		info = json.load(f)
	return jsonify(info)

if __name__ == '__main__':
	app.run() 