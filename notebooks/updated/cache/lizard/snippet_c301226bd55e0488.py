def extract_cite_history(page, extractors):
    appearances = {}
    ids = set()
    for revision in page:
        ids = set(extract_ids(revision.text, extractors))
        for id in ids:
            if id not in appearances:
                appearances[id] = revision.id, revision.timestamp
    for id in ids:
        rev_id, timestamp = appearances[id]
        yield page.id, page.title, rev_id, timestamp, id.type, id.id