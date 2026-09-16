def anchored_pairs(self, anchor):
    pairs = OrderedDict()
    for term in self.keys:
        score = self.get_pair(anchor, term)
        if score:
            pairs[term] = score
    return utils.sort_dict(pairs)