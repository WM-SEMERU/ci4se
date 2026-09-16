def _values(metadata, rel):
    result = []
    for r in metadata:
        if r[REL] == rel:
            result.append(r[VAL])
    return result