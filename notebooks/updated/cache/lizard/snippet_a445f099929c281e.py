def references_to_json(resources, references):
    dump_references = {}
    for reftype, refvalue in references.items():
        dump_references[reftype] = {}
        for label, reference_resource in refvalue.items():
            target_count = len(reference_resource.get_sources(resources))
            dump_references[reftype][label] = dict(count=target_count,
                docname=reference_resource.docname)
    return dump_references