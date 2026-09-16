def get_combo(self, symbol):
    for parent, legs in self.instrument_combos.items():
        if symbol == parent or symbol in legs.keys():
            return {'parent': self.get_instrument(parent), 'legs': legs}
    return {'parent': None, 'legs': {}}