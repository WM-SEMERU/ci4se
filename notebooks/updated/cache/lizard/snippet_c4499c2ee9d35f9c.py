def weighted_choice(self, probabilities, key):
    try:
        choice = self.values[key].lower()
    except KeyError:
        return super(RecordingParameters, self).weighted_choice(probabilities,
            key)
    for probability, option in probabilities:
        if str(option).lower() == choice:
            return option
    for probability, option in probabilities:
        if option.__name__.lower() == choice:
            return option
    assert False, 'Invalid value provided'