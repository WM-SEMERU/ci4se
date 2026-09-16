def searchForMessages(self, query, offset=0, limit=5, thread_id=None):
    message_ids = self.searchForMessageIDs(query, offset=offset, limit=
        limit, thread_id=thread_id)
    for mid in message_ids:
        yield self.fetchMessageInfo(mid, thread_id)