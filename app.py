from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return flask.jsonify({
		'success': True,
		'message': 'Collector works well!'
		'error': -1
	})