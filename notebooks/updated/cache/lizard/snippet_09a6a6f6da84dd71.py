def collection(self, user_id):
    dct = {'userID': user_id, 'page': 0}
    r = 'userGetSongsInLibrary'
    result = self.connection.request(r, dct, self.connection.header(r))
    songs = result[1]['Songs']
    return [Song.from_response(song, self.connection) for song in songs]