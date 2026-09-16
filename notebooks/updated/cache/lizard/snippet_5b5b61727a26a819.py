def normalise(string):
    string = unicodedata.normalize('NFD', string)
    for char_c in ipa.get_precomposed_chars():
        char_d = unicodedata.normalize('NFD', char_c)
        if char_d in string:
            string = string.replace(char_d, char_c)
    return string