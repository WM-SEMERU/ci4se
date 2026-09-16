def get(filename, ignore_fields=None):
    if ignore_fields is None:
        ignore_fields = []
    with open(filename, 'r') as fh:
        bibtex = bibtexparser.load(fh)
    bibtex.entries = [{k: entry[k] for k in entry if k not in ignore_fields
        } for entry in bibtex.entries]
    return bibtex