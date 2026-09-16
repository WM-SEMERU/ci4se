def Query(self, query):
    cursor = self._database.cursor()
    cursor.execute(query)
    return cursor