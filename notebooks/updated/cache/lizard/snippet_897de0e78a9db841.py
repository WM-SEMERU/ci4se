def like(self, photo_id):
    url = '/photos/%s/like' % photo_id
    result = self._post(url)
    return PhotoModel.parse(result)