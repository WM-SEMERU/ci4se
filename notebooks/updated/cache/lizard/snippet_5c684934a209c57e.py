def try_sort_fmt_opts(rdf_format_opts_list, uri):
    filename, file_extension = os.path.splitext(uri)
    if file_extension == '.ttl' or file_extension == '.turtle':
        return ['turtle', 'n3', 'nt', 'json-ld', 'rdfa', 'xml']
    elif file_extension == '.xml' or file_extension == '.rdf':
        return ['xml', 'turtle', 'n3', 'nt', 'json-ld', 'rdfa']
    elif file_extension == '.nt' or file_extension == '.n3':
        return ['n3', 'nt', 'turtle', 'xml', 'json-ld', 'rdfa']
    elif file_extension == '.json' or file_extension == '.jsonld':
        return ['json-ld', 'rdfa', 'n3', 'nt', 'turtle', 'xml']
    elif file_extension == '.rdfa':
        return ['rdfa', 'json-ld', 'n3', 'nt', 'turtle', 'xml']
    else:
        return rdf_format_opts_list