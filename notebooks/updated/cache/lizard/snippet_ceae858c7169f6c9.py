def transform_sparql_update(rdf, update_query):
    logging.debug('performing SPARQL Update transformation')
    if update_query[0] == '@':
        update_query = file(update_query[1:]).read()
    logging.debug('update query: %s', update_query)
    rdf.update(update_query)