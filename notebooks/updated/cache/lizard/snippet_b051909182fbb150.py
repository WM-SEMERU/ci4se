def read(path, corpus=True, index_by='uri', follow_links=False, **kwargs):
    parser = ZoteroParser(path, index_by=index_by, follow_links=follow_links)
    papers = parser.parse()
    if corpus:
        c = Corpus(papers, index_by=index_by, **kwargs)
        if c.duplicate_papers:
            warnings.warn(
                "Duplicate papers detected. Use the 'duplicate_papers' attribute of the corpus to get the list"
                , UserWarning)
        for fset_name, fset_values in parser.full_text.iteritems():
            c.features[fset_name] = StructuredFeatureSet(fset_values)
        return c
    return papers