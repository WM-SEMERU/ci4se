def download(self, song):
    song_id = song['id']
    response = self._call(mm_calls.Export, self.uploader_id, song_id)
    audio = response.body
    suggested_filename = unquote(response.headers['Content-Disposition'].
        split("filename*=UTF-8''")[-1])
    return audio, suggested_filename