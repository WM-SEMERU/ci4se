def _ondim(self, dimension, valuestring):
    try:
        self.dimensions[dimension] = int(valuestring)
    except ValueError:
        self.dimensions[dimension] = 1
        self.textctrls[dimension].SetValue(str(1))
    if self.dimensions[dimension] < 1:
        self.dimensions[dimension] = 1
        self.textctrls[dimension].SetValue(str(1))