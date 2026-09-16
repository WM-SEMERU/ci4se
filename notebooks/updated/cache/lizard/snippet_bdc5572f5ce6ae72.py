def paragraphs(self, with_id=False):
    prevp = 0
    partext = []
    for word, id, pos, lemma in iter(self):
        doc_id, ptype, p, s, w = re.findall(
            '([\\w\\d-]+)\\.(p|head)\\.(\\d+)\\.s\\.(\\d+)\\.w\\.(\\d+)', id)[0
            ]
        if prevp != p and partext:
            yield doc_id + '.' + ptype + '.' + prevp, ' '.join(partext)
            partext = []
        partext.append(word)
        prevp = p
    if partext:
        yield doc_id + '.' + ptype + '.' + prevp, ' '.join(partext)