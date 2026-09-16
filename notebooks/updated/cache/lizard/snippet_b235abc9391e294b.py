def image(alt_text, link_url, title=''):
    image_string = '![' + esc_format(alt_text) + '](' + link_url + ')'
    if title:
        image_string += ' "' + esc_format(title) + '"'
    return image_string