def add_comment(self, comment):
    if 'id' in self._bug:
        self._bugsy.request('bug/{}/comment'.format(self._bug['id']),
            method='POST', json={'comment': comment})
    else:
        self._bug['comment'] = comment