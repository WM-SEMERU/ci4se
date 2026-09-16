def by_id(cls, semantictag_id, autoflush=True):
    query = meta.Session.query(SemanticTag).filter(SemanticTag.id ==
        semantictag_id)
    query = query.autoflush(autoflush)
    semantictag = query.first()
    return semantictag