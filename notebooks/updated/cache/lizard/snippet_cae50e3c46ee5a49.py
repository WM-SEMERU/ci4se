def match(self, origin=None, rel=None, target=None, attrs=None, include_ids
    =False):
    for index, curr_rel in enumerate(self._relationships):
        matches = True
        if origin and origin != curr_rel[ORIGIN]:
            matches = False
            continue
        if rel and rel != curr_rel[RELATIONSHIP]:
            matches = False
            continue
        if target and target != curr_rel[TARGET]:
            matches = False
            continue
        if attrs:
            for k, v in attrs.items():
                if k not in curr_rel[ATTRIBUTES] or curr_rel[ATTRIBUTES].get(k
                    ) != v:
                    matches = False
        if matches:
            if include_ids:
                yield index, (curr_rel[0], curr_rel[1], curr_rel[2],
                    curr_rel[3].copy())
            else:
                yield curr_rel[0], curr_rel[1], curr_rel[2], curr_rel[3].copy()
    return