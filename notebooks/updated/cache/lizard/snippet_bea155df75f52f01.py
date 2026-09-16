def is_noise(self):
    noise = self.args['noise_level']
    if not (self.in_degree and self.out_degree):
        return self.degree > noise
    return False