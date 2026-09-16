def _get_contents(self):

    def files():
        for value in super(GlobBundle, self)._get_contents():
            for path in glob.glob(value):
                yield path
    return list(files())