def update_hierarchy(self, hierarchy_form):
    if self._catalog_session is not None:
        return self._catalog_session.update_catalog(catalog_form=hierarchy_form
            )
    collection = JSONClientValidated('hierarchy', collection='Hierarchy',
        runtime=self._runtime)
    if not isinstance(hierarchy_form, ABCHierarchyForm):
        raise errors.InvalidArgument('argument type is not an HierarchyForm')
    if not hierarchy_form.is_for_update():
        raise errors.InvalidArgument(
            'the HierarchyForm is for update only, not create')
    try:
        if self._forms[hierarchy_form.get_id().get_identifier()] == UPDATED:
            raise errors.IllegalState(
                'hierarchy_form already used in an update transaction')
    except KeyError:
        raise errors.Unsupported(
            'hierarchy_form did not originate from this session')
    if not hierarchy_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    collection.save(hierarchy_form._my_map)
    self._forms[hierarchy_form.get_id().get_identifier()] = UPDATED
    return objects.Hierarchy(osid_object_map=hierarchy_form._my_map,
        runtime=self._runtime, proxy=self._proxy)