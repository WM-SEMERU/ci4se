def get_draft_page_by_id(self, page_id, status='draft'):
    url = 'rest/api/content/{page_id}?status={status}'.format(page_id=
        page_id, status=status)
    return self.get(url)