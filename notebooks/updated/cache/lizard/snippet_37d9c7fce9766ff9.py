def load(cls, path):
    try:
        with open(path, 'rb') as f:
            return cls(__data__=json.loads(f.read().decode('utf-8')))
    except:
        pass
    with open(path, 'rb') as f:
        return cls(__data__=pickle.load(f))