def resolve_doc(cls, manifest, target_doc_name, target_doc_package,
    current_project, node_package):
    if target_doc_package is not None:
        return manifest.find_docs_by_name(target_doc_name, target_doc_package)
    candidate_targets = [current_project, node_package, None]
    target_doc = None
    for candidate in candidate_targets:
        target_doc = manifest.find_docs_by_name(target_doc_name, candidate)
        if target_doc is not None:
            break
    return target_doc