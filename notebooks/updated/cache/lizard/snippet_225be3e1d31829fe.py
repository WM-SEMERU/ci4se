def read_gist_file(self, gist):
    url = False
    files = gist.get('files')
    for gist_file in files:
        if gist_file.get('filename') == self.filename:
            url = gist_file.get('raw_url')
            break
    if url:
        self.output('Reading {}'.format(url))
        response = self.requests.get(url)
        return response.content