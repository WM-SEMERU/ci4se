def get_assignable_gradebook_ids(self, gradebook_id):
    mgr = self._get_provider_manager('GRADING', local=True)
    lookup_session = mgr.get_gradebook_lookup_session(proxy=self._proxy)
    gradebooks = lookup_session.get_gradebooks()
    id_list = []
    for gradebook in gradebooks:
        id_list.append(gradebook.get_id())
    return IdList(id_list)