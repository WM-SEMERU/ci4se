def _what_default(self, pronunciation):
    token_default = self['metadata']['token_default']['what']
    index_count = 2 * len(pronunciation) + 1
    predictions = {}
    for i in range(index_count):
        index_predictions = {}
        if i % 2 == 0:
            index_predictions.update(token_default['0'])
        else:
            presented_phoneme = pronunciation[int((i - 1) / 2)]
            index_predictions[presented_phoneme] = token_default['1']['=']
            index_predictions['*'] = token_default['1']['*']
            index_predictions[''] = token_default['1']['']
        predictions['{}'.format(i)] = index_predictions
    return predictions