def __parse_names():
    filename = get_file('names.tsv.gz')
    with io.open(filename, 'r', encoding='cp1252') as textfile:
        next(textfile)
        for line in textfile:
            tokens = line.strip().split('\t')
            chebi_id = int(tokens[1])
            if chebi_id not in __ALL_NAMES:
                __ALL_NAMES[chebi_id] = []
            nme = Name(tokens[4], tokens[2], tokens[3], tokens[5] == 'T',
                tokens[6])
            __ALL_NAMES[chebi_id].append(nme)