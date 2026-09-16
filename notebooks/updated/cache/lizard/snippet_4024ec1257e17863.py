def list_album_titles(self):
    self.log.info('starting the ``list_album_titles`` method')
    albumList = []
    try:
        response = requests.get(url='https://api.flickr.com/services/rest/',
            params={'method': 'flickr.photosets.getList', 'format': 'json',
            'nojsoncallback': '1'}, auth=self.auth)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    albumList = []
    albumList[:] = [i['title']['_content'] for i in response.json()[
        'photosets']['photoset']]
    self.log.info('completed the ``list_album_titles`` method')
    return albumList