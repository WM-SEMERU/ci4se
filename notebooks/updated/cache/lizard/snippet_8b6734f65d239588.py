def clean(self, text, **kwargs):
    if sys.version_info < (3, 0):
        if not isinstance(text, unicode):
            raise exceptions.UnicodeRequired
    clean_chunks = []
    filth = Filth()
    for next_filth in self.iter_filth(text):
        clean_chunks.append(text[filth.end:next_filth.beg])
        clean_chunks.append(next_filth.replace_with(**kwargs))
        filth = next_filth
    clean_chunks.append(text[filth.end:])
    return ''.join(clean_chunks)