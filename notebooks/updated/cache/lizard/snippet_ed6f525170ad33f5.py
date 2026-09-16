def query(usr, pwd, *hpo_terms):
    raw_result = query_phenomizer(usr, pwd, *hpo_terms)
    for line in raw_result.text.split('\n'):
        if len(line) > 1:
            if not line.startswith('#'):
                yield parse_result(line)