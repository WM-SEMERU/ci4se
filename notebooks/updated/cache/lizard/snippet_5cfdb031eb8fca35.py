def revdocs2reverts(rev_docs, radius=defaults.RADIUS, use_sha1=False,
    resort=False, verbose=False):
    page_rev_docs = groupby(rev_docs, lambda rd: rd.get('page'))
    for page_doc, rev_docs in page_rev_docs:
        if verbose:
            sys.stderr.write(page_doc.get('title') + ': ')
            sys.stderr.flush()
        if resort:
            if verbose:
                sys.stderr.write('(sorting) ')
                sys.stderr.flush()
            rev_docs = sorted(rev_docs, key=lambda r: (r.get('timestamp'),
                r.get('id')))
        detector = Detector(radius=radius)
        for rev_doc in rev_docs:
            if not use_sha1 and 'text' not in rev_doc:
                logger.warn("Skipping {0}: 'text' field not found in {0}".
                    format(rev_doc['id'], rev_doc))
                continue
            if use_sha1:
                checksum = rev_doc.get('sha1') or DummyChecksum()
            elif 'text' in rev_doc:
                text_bytes = bytes(rev_doc['text'], 'utf8', 'replace')
                checksum = hashlib.sha1(text_bytes).digest()
            revert = detector.process(checksum, rev_doc)
            if revert:
                yield revert.to_json()
                if verbose:
                    sys.stderr.write('r')
                    sys.stderr.flush()
            elif verbose:
                sys.stderr.write('.')
                sys.stderr.flush()
        if verbose:
            sys.stderr.write('\n')
            sys.stderr.flush()