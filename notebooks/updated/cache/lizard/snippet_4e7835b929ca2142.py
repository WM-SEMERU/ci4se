def get_cands_list_from_split(session, candidate_classes, doc, split):
    cands = []
    if split == ALL_SPLITS:
        for candidate_class in candidate_classes:
            cands.append(session.query(candidate_class).filter(
                candidate_class.document_id == doc.id).all())
    else:
        for candidate_class in candidate_classes:
            cands.append(session.query(candidate_class).filter(
                candidate_class.document_id == doc.id).filter(
                candidate_class.split == split).all())
    return cands