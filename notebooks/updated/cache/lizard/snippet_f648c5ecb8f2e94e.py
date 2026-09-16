def remove(self, statement_text):
    Statement = self.get_model('statement')
    session = self.Session()
    query = session.query(Statement).filter_by(text=statement_text)
    record = query.first()
    session.delete(record)
    self._session_finish(session)