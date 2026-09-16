def raise_infinitive_error(sentence_str):
    sent_doc = textacy.Doc(sentence_str, lang='en_core_web_lg')
    inf_pattern = '<PART|ADP><VERB>'
    infinitives = textacy.extract.pos_regex_matches(sent_doc, inf_pattern)
    for inf in infinitives:
        if inf[0].text.lower() != 'to':
            continue
        if inf[-1].tag_ != 'VB':
            raise Exception('InfinitivePhraseError')