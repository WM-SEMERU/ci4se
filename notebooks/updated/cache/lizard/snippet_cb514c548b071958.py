def write_playlist_file(self, localdir):
    path = '{0}/playlists'.format(localdir)
    if not os.path.exists(path):
        os.makedirs(path)
    filepath = '{0}/{1}'.format(path, self.gen_filename())
    playlist = open(filepath, 'w')
    for track in self.get_tracks():
        playlist.write('{0}/{1}.mp3\n'.format(os.path.abspath(track.
            gen_localdir(localdir)), track.gen_filename()))
    playlist.close()