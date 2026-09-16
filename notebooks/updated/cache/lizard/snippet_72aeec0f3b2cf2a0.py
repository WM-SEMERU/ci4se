def get_page_ids_by_slug(self, slug):
    ids = self.filter(type='slug', body=slug).values('page_id').annotate(
        max_creation_date=Max('creation_date'))
    return [content['page_id'] for content in ids]