def read_pmid_sentences(pmid_sentences, **drum_args):

    def _set_pmid(statements, pmid):
        for stmt in statements:
            for evidence in stmt.evidence:
                evidence.pmid = pmid
    run_drum = drum_args.get('run_drum', False)
    drum_process = None
    all_statements = {}
    for pmid, sentences in pmid_sentences.items():
        logger.info('================================')
        logger.info('Processing %d sentences for %s' % (len(sentences), pmid))
        ts = time.time()
        drum_args['name'] = 'DrumReader%s' % pmid
        dr = DrumReader(**drum_args)
        time.sleep(3)
        if run_drum and drum_process is None:
            drum_args.pop('run_drum', None)
            drum_process = dr.drum_system
            drum_args['drum_system'] = drum_process
        for sentence in sentences:
            dr.read_text(sentence)
        try:
            dr.start()
        except SystemExit:
            pass
        statements = []
        for extraction in dr.extractions:
            if not extraction:
                continue
            tp = process_xml(extraction)
            statements += tp.statements
        _set_pmid(statements, pmid)
        te = time.time()
        logger.info('Reading took %d seconds and produced %d Statements.' %
            (te - ts, len(statements)))
        all_statements[pmid] = statements
    if drum_process and dr.drum_system:
        dr._kill_drum()
    return all_statements