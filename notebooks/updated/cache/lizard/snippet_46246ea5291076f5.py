def is_participle_clause_fragment(sentence):
    if not _begins_with_one_of(sentence, ['VBG', 'VBN', 'JJ']):
        return 0.0
    if _begins_with_one_of(sentence, ['JJ']):
        doc = nlp(sentence)
        fw = [w for w in doc][0]
        if fw.dep_ == 'amod':
            return 0.0
    if _begins_with_one_of(sentence, ['VBG']):
        doc = nlp(sentence)
        fw = [w for w in doc][0]
        if fw.dep_.endswith('subj'):
            return 0.0
        fc = [c for c in doc.noun_chunks]
        if str(fw) in str(fc):
            return 0.0
    positive_prob = models['participle'].predict([_text_to_vector(sentence,
        trigram2idx['participle'], trigram_count['participle'])])[0][1]
    return float(positive_prob)