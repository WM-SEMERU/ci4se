def cmd_guess_labels(*args):
    args = list(args)
    apply_labels = False
    if '--apply' in args:
        apply_labels = True
        args.remove('--apply')
    docid = args[0]
    dsearch = get_docsearch()
    doc = dsearch.get(docid)
    if doc is None:
        raise Exception('Document {} not found. Cannot guess labels'.format
            (docid))
    verbose('Current labels: {}'.format(', '.join([label.name for label in
        doc.labels])))
    guessed = dsearch.guess_labels(doc)
    verbose('Guessed labels: {}'.format(', '.join([label.name for label in
        guessed])))
    r = {'docid': doc.docid, 'current_labels': [label.name for label in doc
        .labels], 'guessed_labels': [label.name for label in guessed],
        'applied': 'yes' if apply_labels else 'no'}
    changed = False
    if apply_labels:
        for label in guessed:
            if label not in doc.labels:
                dsearch.add_label(doc, label, update_index=False)
                changed = True
        for label in doc.labels:
            if label not in guessed:
                dsearch.remove_label(doc, label, update_index=False)
                changed = True
    if changed:
        index_updater = dsearch.get_index_updater(optimize=False)
        index_updater.upd_doc(doc)
        index_updater.commit()
        verbose('Document {} updated'.format(docid))
    elif apply_labels:
        verbose('Document {} unchanged'.format(docid))
    reply(r)