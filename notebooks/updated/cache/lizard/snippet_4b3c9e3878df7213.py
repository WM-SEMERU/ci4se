def dump_simple_db(path):
    output = []
    simpledb = SimpleDb(path, mode='r', sync=False)
    with simpledb as db:
        for key in db:
            output.append('{0}: {1}'.format(key, db.dumpvalue(key)))
    return '\n'.join(output)