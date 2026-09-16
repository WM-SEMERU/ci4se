def read_targets(targets):
    results = {}
    for target, regexer in regexer_for_targets(targets):
        with open(target) as fh:
            results.update(extract_keypairs(fh.readlines(), regexer))
    return results