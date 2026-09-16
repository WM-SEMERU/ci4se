def get_albums(self, *args, **kwargs):
    args = tuple(['albums'] + list(args))
    return self.get_music_library_information(*args, **kwargs)