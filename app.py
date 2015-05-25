from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        'success': True,
        'message': 'Collector works well!',
        'error': -1
    })