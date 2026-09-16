def reactToAMQPMessage(req, send_back):
    if not _iiOfAny(req, REQUEST_TYPES):
        raise ValueError("Unknown type of request: '" + str(type(req)) + "'!")
    if _iiOfAny(req, CountRequest) and _iiOfAny(req.query, QUERY_TYPES):
        return req.query.getCountResult()
    elif _iiOfAny(req, SearchRequest) and _iiOfAny(req.query, QUERY_TYPES):
        return req.query.getSearchResult()
    elif _iiOfAny(req, ISBNValidationRequest):
        ISBN = req.ISBN
        if _iiOfAny(ISBN, ISBNQuery):
            ISBN = ISBN.ISBN
        return ISBNValidationResult(isbn_validator.is_valid_isbn(ISBN))
    elif _iiOfAny(req, ExportRequest):
        export.exportEPublication(req.epublication)
        return ExportResult(req.epublication.ISBN)
    raise ValueError("Unknown type of request: '" + str(type(req)) +
        "' or query: '" + str(type(req.query)) + "'!")