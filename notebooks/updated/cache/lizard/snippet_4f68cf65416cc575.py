def load(filepath=None, filecontent=None):
    conf = DotDict()
    assert filepath or filecontent
    if not filecontent:
        with io.FileIO(filepath) as handle:
            filecontent = handle.read().decode('utf-8')
    configs = json.loads(filecontent)
    conf.update(configs.items())
    return conf