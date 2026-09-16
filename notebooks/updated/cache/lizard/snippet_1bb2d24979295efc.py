def OutputDocumentFor(objs, apply_theme=None, always_new=False):
    if not isinstance(objs, collections_abc.Sequence) or len(objs
        ) == 0 or not all(isinstance(x, Model) for x in objs):
        raise ValueError('OutputDocumentFor expects a sequence of Models')

    def finish():
        pass
    docs = set(x.document for x in objs)
    if None in docs:
        docs.remove(None)
    if always_new:

        def finish():
            _dispose_temp_doc(objs)
        doc = _create_temp_doc(objs)
    elif len(docs) == 0:
        doc = Document()
        for model in objs:
            doc.add_root(model)
    elif len(docs) == 1:
        doc = docs.pop()
        if set(objs) != set(doc.roots):

            def finish():
                _dispose_temp_doc(objs)
            doc = _create_temp_doc(objs)
        pass
    else:

        def finish():
            _dispose_temp_doc(objs)
        doc = _create_temp_doc(objs)
    if settings.perform_document_validation():
        doc.validate()
    _set_temp_theme(doc, apply_theme)
    yield doc
    _unset_temp_theme(doc)
    finish()