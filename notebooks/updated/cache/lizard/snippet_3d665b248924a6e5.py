def get_json(self):
    port = self.get_basic_json()
    port['Functions'] = {'Function': [f.get_json() for f in self.functions.
        values()]}
    return port