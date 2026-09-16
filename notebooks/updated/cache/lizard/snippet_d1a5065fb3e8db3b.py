def delete(self, mutagen_file):
    for cover_tag in self.TAG_NAMES.values():
        try:
            del mutagen_file[cover_tag]
        except KeyError:
            pass