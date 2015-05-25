from flask import Flask, jsonify
import steammarket

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        'success': True,
        'message': 'Collector works well!',
        'error': -1
    })


@app.route('/get-listing')
def get_listing():
    listing = steammarket.get_listing()

    if listing:
        return jsonify({
            'success': True,
            'listing': listing,
            'message': '',
            'error': -1
        })

    return jsonify({
        'success': False,
        'message': 'No listings presented',
        'error': 1
    })