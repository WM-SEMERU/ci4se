def disjoint_relations(rdf, fix=False):
    for conc1, conc2 in sorted(rdf.subject_objects(SKOS.related)):
        if conc2 in sorted(rdf.transitive_objects(conc1, SKOS.broader)):
            if fix:
                logging.warning(
                    'Concepts %s and %s connected by both skos:broaderTransitive and skos:related, removing skos:related'
                    , conc1, conc2)
                rdf.remove((conc1, SKOS.related, conc2))
                rdf.remove((conc2, SKOS.related, conc1))
            else:
                logging.warning(
                    'Concepts %s and %s connected by both skos:broaderTransitive and skos:related, but keeping it because keep_related is enabled'
                    , conc1, conc2)