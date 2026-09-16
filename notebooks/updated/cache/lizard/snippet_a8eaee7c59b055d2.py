def generate_text(self, max_length=None):
    return self._text_generator(next_token=self._generate_next_token,
        max_length=max_length)