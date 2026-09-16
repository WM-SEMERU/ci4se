def encode1(self):
    data_uri = b64encode(open(self.path, 'rb').read()).decode('utf-8').replace(
        '\n', '')
    return '<img src="data:image/png;base64,{0}">'.format(data_uri)