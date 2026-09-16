def get_random(self):
    num_kittens = self.count()
    new_cutoff = num_kittens / (num_kittens + constants.KITTEN_FRESHNESS)
    if random.random() < new_cutoff:
        return self._rand_inst()
    else:
        return self.create_new()