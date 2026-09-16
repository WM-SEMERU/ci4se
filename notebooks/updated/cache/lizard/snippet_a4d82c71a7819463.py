def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id, proxy
    ):
    if not self.supports_gradebook_column_lookup():
        raise errors.Unimplemented()
    return sessions.GradebookColumnLookupSession(gradebook_id, proxy, self.
        _runtime)