def put_text(self, key, text):
    with open(key, 'w') as fh:
        fh.write(text)