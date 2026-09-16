def load_stream(cls, st):
    y = yaml.load(st)
    return [Automaton(k, v) for k, v in y.iteritems()]