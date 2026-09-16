def _process_layperson_results(self, results):
    payload = {'results': []}
    for doc in results.docs:
        hl = self._process_highlight(results, doc)
        highlight = {'id': doc['id'], 'highlight': hl.highlight, 'label':
            doc['label'], 'matched_synonym': hl.match}
        payload['results'].append(highlight)
    logging.debug('Docs: {}'.format(len(results.docs)))
    return payload