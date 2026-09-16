def reload(filename=None, url=
    'https://raw.githubusercontent.com/googlei18n/emoji4unicode/master/data/emoji4unicode.xml'
    , loader_class=None):
    u
    if loader_class is None:
        loader_class = loader.Loader
    global _loader
    _loader = loader_class()
    _loader.load(filename, url)