def docs_repr(*args):
    sio = StringIO()
    for doc_idx, doc in enumerate(args):
        if doc_idx > 0:
            sio.write(', ')
        sio.write(text_type(json_util.dumps(doc)))
    return sio.getvalue()