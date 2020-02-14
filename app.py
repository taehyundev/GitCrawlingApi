from flask import Flask, render_template, jsonify, make_response, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl
import re
import json
from modules import crawling
app = Flask(__name__)

#'/'는 index Page
@app.route('/')
def index():
	return render_template('index.html')

#Commit 결과 보기
@app.route('/commit_result')
def test():
	with open('data/commit_result.json', 'r',encoding='utf-8') as f:
		info = json.load(f)
	return json.dumps(info,indent='\t',ensure_ascii=False)

#Commit 내용 Update
@app.route('/commmit_update')
def commit_update():
	crawling.Crawling_git()
	print("Success")
	return  render_template('index.html')


@app.route('/api/commit', methods=['GET'])
def commitapi(): 
	with open('data/commit_result.json', 'r',encoding='utf-8') as f:
		info = json.load(f)
	return jsonify(info)

#Main
if __name__ == '__main__':
	with open('data/private_data.json', 'r',encoding='utf-8') as f:
		privatedata = json.load(f)
	app.run(host=privatedata["ip"],port = privatedata["port"]) 
	#private_data라는 json파일을 사용하여 app.run을 함