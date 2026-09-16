def update(self, statement):
    Statement = self.get_model('statement')
    Tag = self.get_model('tag')
    if statement is not None:
        session = self.Session()
        record = None
        if hasattr(statement, 'id') and statement.id is not None:
            record = session.query(Statement).get(statement.id)
        else:
            record = session.query(Statement).filter(Statement.text ==
                statement.text, Statement.conversation == statement.
                conversation).first()
            if not record:
                record = Statement(text=statement.text, conversation=
                    statement.conversation, persona=statement.persona)
        record.in_response_to = statement.in_response_to
        record.created_at = statement.created_at
        record.search_text = self.tagger.get_bigram_pair_string(statement.text)
        if statement.in_response_to:
            record.search_in_response_to = self.tagger.get_bigram_pair_string(
                statement.in_response_to)
        for tag_name in statement.get_tags():
            tag = session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            record.tags.append(tag)
        session.add(record)
        self._session_finish(session)