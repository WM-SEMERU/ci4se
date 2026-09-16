def add_arxiv_eprint(self, arxiv_id, arxiv_categories):
    self._append_to('arxiv_eprints', {'value': arxiv_id, 'categories':
        arxiv_categories})
    self.set_citeable(True)