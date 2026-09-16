def encipher(self, string):
    string = self.remove_punctuation(string)
    ret = ''
    for c in range(0, len(string)):
        ret += self.encipher_char(string[c])
    return ret