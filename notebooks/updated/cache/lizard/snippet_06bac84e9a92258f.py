def translate_detector(self, vector):
    vector = np.array(vector, dtype=float)
    self.pmts.pos_x += vector[0]
    self.pmts.pos_y += vector[1]
    self.pmts.pos_z += vector[2]
    self.reset_caches()