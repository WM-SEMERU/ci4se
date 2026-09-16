def pad_sentences(sentences, padding_word='</s>'):
    sequence_length = max(len(x) for x in sentences)
    padded_sentences = []
    for i, sentence in enumerate(sentences):
        num_padding = sequence_length - len(sentence)
        new_sentence = sentence + [padding_word] * num_padding
        padded_sentences.append(new_sentence)
    return padded_sentences