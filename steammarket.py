import utils


def get_listing():
    listing = utils.open_file_line('listings.txt')
    return listing