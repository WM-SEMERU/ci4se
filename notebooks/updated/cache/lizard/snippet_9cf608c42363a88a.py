def update_family(self, family_form):
    if self._catalog_session is not None:
        return self._catalog_session.update_catalog(catalog_form=family_form)
    collection = JSONClientValidated('relationship', collection='Family',
        runtime=self._runtime)
    if not isinstance(family_form, ABCFamilyForm):
        raise errors.InvalidArgument('argument type is not an FamilyForm')
    if not family_form.is_for_update():
        raise errors.InvalidArgument(
            'the FamilyForm is for update only, not create')
    try:
        if self._forms[family_form.get_id().get_identifier()] == UPDATED:
            raise errors.IllegalState(
                'family_form already used in an update transaction')
    except KeyError:
        raise errors.Unsupported(
            'family_form did not originate from this session')
    if not family_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    collection.save(family_form._my_map)
    self._forms[family_form.get_id().get_identifier()] = UPDATED
    return objects.Family(osid_object_map=family_form._my_map, runtime=self
        ._runtime, proxy=self._proxy)