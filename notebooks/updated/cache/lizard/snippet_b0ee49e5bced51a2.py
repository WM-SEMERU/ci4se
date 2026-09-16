def decipher(self, string):
    string = self.remove_punctuation(string, filter='[^' + self.chars + ']')
    ret = ''
    for i in range(0, len(string), 3):
        ind = tuple([int(string[i + k]) for k in [0, 1, 2]])
        ret += IND2L[ind]
    return ret