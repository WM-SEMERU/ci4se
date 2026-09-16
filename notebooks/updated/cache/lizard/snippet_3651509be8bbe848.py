def get_gradebooks_by_grade_system(self, grade_system_id):
    mgr = self._get_provider_manager('GRADING', local=True)
    lookup_session = mgr.get_gradebook_lookup_session(proxy=self._proxy)
    return lookup_session.get_gradebooks_by_ids(self.
        get_gradebook_ids_by_grade_system(grade_system_id))