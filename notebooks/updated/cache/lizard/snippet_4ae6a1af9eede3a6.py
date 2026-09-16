def get_all_comments_of_incoming(self, incoming_id):
    return self._iterate_through_pages(get_function=self.
        get_comments_of_incoming_per_page, resource=INCOMING_COMMENTS, **{
        'incoming_id': incoming_id})