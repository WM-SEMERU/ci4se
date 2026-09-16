def set_page_artid(self, page_start=None, page_end=None, artid=None):
    if page_end and not page_start:
        raise ValueError('End_page provided without start_page')
    self._ensure_reference_field('publication_info', {})
    publication_info = self.obj['reference']['publication_info']
    if page_start:
        publication_info['page_start'] = page_start
    if page_end:
        publication_info['page_end'] = page_end
    if artid:
        publication_info['artid'] = artid