def find_input_documents(self):
    paths = []
    itr = chain(texutils.input_pattern.finditer(self.text), texutils.
        input_ifexists_pattern.finditer(self.text))
    for match in itr:
        fname = match.group(1)
        if not fname.endswith('.tex'):
            full_fname = '.'.join((fname, 'tex'))
        else:
            full_fname = fname
        paths.append(full_fname)
    return paths