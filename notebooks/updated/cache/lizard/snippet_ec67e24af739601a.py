def by_tag_id(self, tag_id):
    query = meta.Session.query(TagSemanticTag).filter(TagSemanticTag.tag_id ==
        tag_id)
    return query.first()