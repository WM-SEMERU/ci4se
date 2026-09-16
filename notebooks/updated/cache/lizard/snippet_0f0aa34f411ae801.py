def _LineWrap(text, width):
    return reduce(lambda line, word, width=width: '%s%s%s' % (line, ' \n'[
        len(line) - line.rfind('\n') - 1 + len(word.split('\n', 1)[0]) >=
        width], word), text.split(' '))