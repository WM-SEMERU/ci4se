def load(file):
    with open(file, 'r') as f:
        contents = f.read()
    lambder.load_events(contents)