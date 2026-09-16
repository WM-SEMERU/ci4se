def create_concept_scheme(rdf, ns, lname=''):
    ont = None
    if not ns:
        onts = list(rdf.subjects(RDF.type, OWL.Ontology))
        if len(onts) > 1:
            onts.sort()
            ont = onts[0]
            logging.warning(
                'Multiple owl:Ontology instances found. Creating concept scheme from %s.'
                , ont)
        elif len(onts) == 1:
            ont = onts[0]
        else:
            ont = None
        if not ont:
            logging.info(
                'No skos:ConceptScheme or owl:Ontology found. Using namespace auto-detection for creating concept scheme.'
                )
            ns = detect_namespace(rdf)
        elif ont.endswith('/') or ont.endswith('#') or ont.endswith(':'):
            ns = ont
        else:
            ns = ont + '/'
    NS = Namespace(ns)
    cs = NS[lname]
    rdf.add((cs, RDF.type, SKOS.ConceptScheme))
    if ont is not None:
        rdf.remove((ont, RDF.type, OWL.Ontology))
        for o in rdf.objects(ont, OWL.imports):
            rdf.remove((ont, OWL.imports, o))
        for p, o in rdf.predicate_objects(ont):
            prot = URIRef('http://protege.stanford.edu/plugins/owl/protege#')
            if p.startswith(prot):
                rdf.remove((ont, p, o))
        replace_uri(rdf, ont, cs)
    return cs