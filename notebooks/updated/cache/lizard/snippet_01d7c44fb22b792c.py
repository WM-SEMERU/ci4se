def mixedcase(path):
    words = path.split('_')
    return words[0] + ''.join(word.title() for word in words[1:])