def dedupe(contains_dupes, threshold=70, scorer=fuzz.token_set_ratio):
    extractor = []
    for item in contains_dupes:
        matches = extract(item, contains_dupes, limit=None, scorer=scorer)
        filtered = [x for x in matches if x[1] > threshold]
        if len(filtered) == 1:
            extractor.append(filtered[0][0])
        else:
            filtered = sorted(filtered, key=lambda x: x[0])
            filter_sort = sorted(filtered, key=lambda x: len(x[0]), reverse
                =True)
            extractor.append(filter_sort[0][0])
    keys = {}
    for e in extractor:
        keys[e] = 1
    extractor = keys.keys()
    if len(extractor) == len(contains_dupes):
        return contains_dupes
    else:
        return extractor