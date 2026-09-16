def identifier_director(**kwargs):
    qualifier = kwargs.get('qualifier', '')
    content = kwargs.get('content', '')
    if qualifier == 'ISBN':
        return CitationISBN(content=content)
    elif qualifier == 'ISSN':
        return CitationISSN(content=content)
    elif qualifier == 'DOI':
        return CitationDOI(content=content)
    elif qualifier == 'REP-NO':
        return CitationTechnicalReportNumber(content=content)
    else:
        return None