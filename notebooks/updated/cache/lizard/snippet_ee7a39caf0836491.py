def encode(binary):
    encoded = io.BytesIO()
    gzip_file = dict(mode='wb', fileobj=encoded, compresslevel=LEVEL)
    with gzip.GzipFile(**gzip_file) as file_:
        file_.write(binary)
    encoded.seek(0)
    return encoded.read()