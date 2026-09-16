def tags(self, ticket_id):
    return self._query_zendesk(self.endpoint.tags, 'tag', id=ticket_id)