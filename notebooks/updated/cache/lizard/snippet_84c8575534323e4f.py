def matches(self, query):
    thread_query = 'thread:{tid} AND {subquery}'.format(tid=self._id,
        subquery=query)
    num_matches = self._dbman.count_messages(thread_query)
    return num_matches > 0