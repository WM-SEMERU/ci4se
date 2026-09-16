def build_trees_from_text(text, layer, **kwargs):
    from estnltk.text import Text
    assert isinstance(text, Text
        ), "(!) Unexpected text argument! Should be Estnltk's Text object."
    assert layer in text, '(!) The layer ' + str(layer
        ) + ' is missing from the input text.'
    text_sentences = list(text.divide(layer=WORDS, by=SENTENCES))
    all_sentence_trees = []
    prev_sent_id = -1
    norm_prev_sent_id = -1
    current_sentence = []
    k = 0
    while k < len(text[layer]):
        node_desc = text[layer][k]
        if prev_sent_id != node_desc[SENT_ID] and current_sentence:
            norm_prev_sent_id += 1
            assert norm_prev_sent_id < len(text_sentences
                ), '(!) Sentence with the index ' + str(norm_prev_sent_id
                ) + ' not found from the input text.'
            sentence = text_sentences[norm_prev_sent_id]
            trees_of_sentence = build_trees_from_sentence(sentence,
                current_sentence, layer, sentence_id=norm_prev_sent_id, **
                kwargs)
            all_sentence_trees.extend(trees_of_sentence)
            current_sentence = []
        current_sentence.append(node_desc)
        prev_sent_id = node_desc[SENT_ID]
        k += 1
    if current_sentence:
        norm_prev_sent_id += 1
        assert norm_prev_sent_id < len(text_sentences
            ), '(!) Sentence with the index ' + str(norm_prev_sent_id
            ) + ' not found from the input text.'
        sentence = text_sentences[norm_prev_sent_id]
        trees_of_sentence = build_trees_from_sentence(sentence,
            current_sentence, layer, sentence_id=norm_prev_sent_id, **kwargs)
        all_sentence_trees.extend(trees_of_sentence)
    return all_sentence_trees