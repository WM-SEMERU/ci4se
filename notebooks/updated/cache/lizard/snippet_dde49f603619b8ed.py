def generate_trimmer(word_characters):
    start_re = '^[^{}]+'.format(word_characters)
    end_re = '[^{}]+$'.format(word_characters)

    def trimmer(token, i=None, tokens=None):

        def trim(s, metadata=None):
            s = re.sub(start_re, '', s)
            s = re.sub(end_re, '', s)
            return s
        return token.update(trim)
    return trimmer