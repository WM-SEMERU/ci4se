def drop_indexes(quiet=True, stdout=None):
    results, meta = db.cypher_query('CALL db.indexes()')
    pattern = re.compile(':(.*)\\((.*)\\)')
    for index in results:
        db.cypher_query('DROP ' + index[0])
        match = pattern.search(index[0])
        stdout.write(' - Dropping index on label {0} with property {1}.\n'.
            format(match.group(1), match.group(2)))
    stdout.write('\n')