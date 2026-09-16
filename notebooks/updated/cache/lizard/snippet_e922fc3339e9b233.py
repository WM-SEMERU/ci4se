def get_stable_id(self):
    return construct_stable_id(self.sentence, self.
        _get_polymorphic_identity(), self.char_start, self.char_end)