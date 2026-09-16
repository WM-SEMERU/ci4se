def add_search_engine(self, name, engine):
    if engine is None:
        self.search_engines.pop(name, None)
    self.search_engines[name] = engine
    return self