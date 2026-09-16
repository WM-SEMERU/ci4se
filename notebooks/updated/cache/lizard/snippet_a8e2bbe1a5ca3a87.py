def extract(query, choices, processor=default_processor, scorer=
    default_scorer, limit=5):
    sl = extractWithoutOrder(query, choices, processor, scorer)
    return heapq.nlargest(limit, sl, key=lambda i: i[1]
        ) if limit is not None else sorted(sl, key=lambda i: i[1], reverse=True
        )