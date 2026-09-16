def text(self, max_nb_chars=200, ext_word_list=None):
    text = []
    if max_nb_chars < 5:
        raise ValueError(
            'text() can only generate text of at least 5 characters')
    if max_nb_chars < 25:
        while not text:
            size = 0
            while size < max_nb_chars:
                word = (self.word_connector if size else '') + self.word(
                    ext_word_list=ext_word_list)
                text.append(word)
                size += len(word)
            text.pop()
        text[0] = text[0][0].upper() + text[0][1:]
        last_index = len(text) - 1
        text[last_index] += self.sentence_punctuation
    elif max_nb_chars < 100:
        while not text:
            size = 0
            while size < max_nb_chars:
                sentence = (self.word_connector if size else ''
                    ) + self.sentence(ext_word_list=ext_word_list)
                text.append(sentence)
                size += len(sentence)
            text.pop()
    else:
        while not text:
            size = 0
            while size < max_nb_chars:
                paragraph = ('\n' if size else '') + self.paragraph(
                    ext_word_list=ext_word_list)
                text.append(paragraph)
                size += len(paragraph)
            text.pop()
    return ''.join(text)