def chain(tree, edition_number):
    return sorted(tree.get(edition_number, []), key=lambda d: d[
        'timestamp_utc'])