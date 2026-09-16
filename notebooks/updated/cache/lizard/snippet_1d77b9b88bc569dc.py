def _delete_text_ngrams(self, text_id):
    with self._conn:
        self._conn.execute(constants.DELETE_TEXT_NGRAMS_SQL, [text_id])
        self._conn.execute(constants.DELETE_TEXT_HAS_NGRAMS_SQL, [text_id])