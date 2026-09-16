def from_dict(d):
    query_params_match = d.get('@query_params_match')
    sources = [Source.from_dict(source) for source in d.get('sources', [])]
    fields = Person.fields_from_dict(d)
    return Person(fields=fields, sources=sources, query_params_match=
        query_params_match)