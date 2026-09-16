def sentence_bytes(self, sentence):
    result = [TOKENS[sentence[0]]]
    for i in sentence[1:]:
        if isinstance(i, str):
            result.extend(self.literal(i))
        elif isinstance(i, float) or isinstance(i, int):
            result.extend(self.number(i))
        else:
            result.extend(i)
    return result