def __replace_nouns(sentence, counts):
    if sentence is not None:
        while sentence.find('#NOUN') != -1:
            sentence = sentence.replace('#NOUN', str(__get_noun(counts)), 1)
            if sentence.find('#NOUN') == -1:
                return sentence
        return sentence
    else:
        return sentence