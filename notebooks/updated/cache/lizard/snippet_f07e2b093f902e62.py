def filter_publication(publication, cmp_authors=True):
    query = None
    isbn_query = False
    if publication.optionals and publication.optionals.ISBN:
        query = aleph.ISBNQuery(publication.optionals.ISBN)
        isbn_query = True
    else:
        query = aleph.TitleQuery(publication.title)
    result = aleph.reactToAMQPMessage(aleph.SearchRequest(query), '')
    if not result.records:
        return publication
    if isbn_query:
        for record in result.records:
            epub = record.epublication
            if compare_names(epub.nazev, publication.title) >= 80:
                return None
        return publication
    for record in result.records:
        epub = record.epublication
        if not compare_names(epub.nazev, publication.title) >= 80:
            continue
        if not cmp_authors:
            return None
        for author in epub.autori:
            author_str = '%s %s %s' % (author.firstName, author.lastName,
                author.title)
            pub_authors = map(lambda x: x.name, publication.authors)
            if type(pub_authors) not in [list, tuple, set]:
                pub_authors = [pub_authors]
            for pub_author in pub_authors:
                if compare_names(author_str, pub_author) >= 50:
                    return None
    return publication