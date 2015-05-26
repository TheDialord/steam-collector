import utils
LISTINGS_PATH = 'listings.json'
ITEMS_PATH = 'items.json'

def get_listing():
    listing = utils.open_file_line(LISTINGS_PATH)
    return listing


def add_listing(listing_id, price_subtotal, price_fee):
    return utils.add_file_line(LISTINGS_PATH, {
        'id': listing_id,
        'subtotal': price_subtotal,
        'fee': price_fee,
        'total': price_subtotal + price_fee,
        'quantity': 1
    })


def load_items():
    return utils.open_items(ITEMS_PATH)