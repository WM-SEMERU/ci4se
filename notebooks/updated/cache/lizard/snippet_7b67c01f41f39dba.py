def _match_dialog(self, query, dialogues=None):
    if dialogues is None:
        dialogues = self._dialogues
    if query in dialogues:
        response = dialogues[query]
        logger.debug('Found response in queries: %s' % repr(response))
        return response