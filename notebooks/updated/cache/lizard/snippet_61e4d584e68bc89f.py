def cleanup_unreachable(rdf):
    all_subjects = set(rdf.subjects())
    logging.debug('total subject resources: %d', len(all_subjects))
    reachable = find_reachable(rdf, SKOS.Concept)
    nonreachable = all_subjects - reachable
    logging.debug('deleting %s non-reachable resources', len(nonreachable))
    for subj in nonreachable:
        delete_uri(rdf, subj)