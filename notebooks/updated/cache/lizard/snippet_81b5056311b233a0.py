def registergrant(source=None, setspec=None):
    with open(source, 'r') as fp:
        data = json.load(fp)
    register_grant(data)