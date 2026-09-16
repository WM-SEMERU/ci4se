def get_gradebooks_by_parent_genus_type(self, *args, **kwargs):
    catalogs = self._get_provider_session('gradebook_lookup_session'
        ).get_gradebooks_by_parent_genus_type(*args, **kwargs)
    cat_list = []
    for cat in catalogs:
        cat_list.append(Gradebook(self._provider_manager, cat, self.
            _runtime, self._proxy))
    return GradebookList(cat_list)