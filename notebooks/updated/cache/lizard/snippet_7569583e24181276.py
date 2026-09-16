def _symbols_for_image(image):
    symbol = zbar_image_first_symbol(image)
    while symbol:
        yield symbol
        symbol = zbar_symbol_next(symbol)