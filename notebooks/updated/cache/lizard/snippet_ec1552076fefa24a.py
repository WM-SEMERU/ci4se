def tags(self):
    ch, I, O, B = self.chunk, INSIDE + '-', OUTSIDE, BEGIN + '-'
    tags = [OUTSIDE for i in range(len(self.sentence.token))]
    for i, tag in enumerate(self.sentence.token):
        if tag == WORD:
            tags[i] = encode_entities(self.string)
        elif tag == POS and self.type:
            tags[i] = self.type
        elif tag == CHUNK and ch and ch.type:
            tags[i] = (self == ch[0] and B or I) + ch.type
        elif tag == PNP and self.pnp:
            tags[i] = (self == self.pnp[0] and B or I) + 'PNP'
        elif tag == REL and ch and len(ch.relations) > 0:
            tags[i] = ['-'.join([str(x) for x in [ch.type] + list(reversed(
                r)) if x]) for r in ch.relations]
            tags[i] = '*'.join(tags[i])
        elif tag == ANCHOR and ch:
            tags[i] = ch.anchor_id or OUTSIDE
        elif tag == LEMMA:
            tags[i] = encode_entities(self.lemma or '')
        elif tag in self.custom_tags:
            tags[i] = self.custom_tags.get(tag) or OUTSIDE
    return tags