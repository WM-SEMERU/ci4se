def get_all_draft_pages_from_space(self, space, start=0, limit=500, status=
    'draft'):
    return self.get_all_pages_from_space(space, start, limit, status)