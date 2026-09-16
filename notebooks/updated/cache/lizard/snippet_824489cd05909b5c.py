def _disambiguate_doc(self, tagged_tokens):
    pos_groups = {pos: [] for pos in [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]}
    for tok, tag in tagged_tokens:
        if tag in pos_groups:
            pos_groups[tag].append(tok)
    map = {}
    for tag, toks in pos_groups.items():
        map.update(self._disambiguate_pos(toks, tag))
    return map