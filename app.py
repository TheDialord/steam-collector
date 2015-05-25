from flask import Flask, jsonify
import steammarket

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'success': True,
        'message': 'Collector works well!',
        'error': -1
    })


@app.route('/get-listing', methods=['GET'])
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


@app.route('/add-listing/<int:listing_id><int:price_subtotal>/<int:price_fee>', methods=['GET'])
def add_listing(listing_id, price_subtotal, price_fee):
    result = steammarket.add_listing(listing_id, price_subtotal, price_fee)

    if result:
        return jsonify({
            'success': True,
            'message': 'Added',
            'error': -1
        })

    return jsonify({
        'success': False,
        'message': 'Unknown error',
        'error': 2
    })