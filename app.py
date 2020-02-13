import json
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
	return "Crawling"

@app.route('/commit_result', methods=['GET'])
def test():
	with open('data/commit_result.json', 'r') as f:
		r_info = json.load(f)
	return render_template('post.html',testDataHtml = r_info)

if __name__ == '__main__':
	app.run() 