def get_batch(sequence, size, start=0, endpoint=None, complete=False):
    batch = make_batch(sequence, size, start)
    return {'pagesize': batch.get_pagesize(), 'next': batch.make_next_url(),
        'previous': batch.make_prev_url(), 'page': batch.get_pagenumber(),
        'pages': batch.get_numpages(), 'count': batch.get_sequence_length(),
        'items': make_items_for([b for b in batch.get_batch()], endpoint,
        complete=complete)}