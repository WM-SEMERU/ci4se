def drop_modifiers(sentence_str):
    tdoc = textacy.Doc(sentence_str, lang='en_core_web_lg')
    new_sent = tdoc.text
    unusual_char = '形'
    for tag in tdoc:
        if tag.dep_.endswith('mod'):
            new_sent = new_sent[:tag.idx] + unusual_char * len(tag.text
                ) + new_sent[tag.idx + len(tag.text):]
    new_sent = new_sent.replace(unusual_char, '')
    new_sent = textacy.preprocess.normalize_whitespace(new_sent)
    return new_sent