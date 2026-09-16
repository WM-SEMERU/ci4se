def parse_stream(stream, format='Jæren Sparebank'):
    Class = formats[format.lower()]
    return Class.csv_to_transactions(stream)