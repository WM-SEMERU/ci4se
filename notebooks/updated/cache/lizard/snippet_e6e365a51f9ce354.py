def decode(self, encoder):
    self.matrix = [encoder.inverse_transform(row) for row in self.matrix]