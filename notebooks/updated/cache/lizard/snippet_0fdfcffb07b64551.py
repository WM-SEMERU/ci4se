def update_gradebook_column(self, gradebook_column_form):
    collection = JSONClientValidated('grading', collection=
        'GradebookColumn', runtime=self._runtime)
    if not isinstance(gradebook_column_form, ABCGradebookColumnForm):
        raise errors.InvalidArgument(
            'argument type is not an GradebookColumnForm')
    if not gradebook_column_form.is_for_update():
        raise errors.InvalidArgument(
            'the GradebookColumnForm is for update only, not create')
    try:
        if self._forms[gradebook_column_form.get_id().get_identifier()
            ] == UPDATED:
            raise errors.IllegalState(
                'gradebook_column_form already used in an update transaction')
    except KeyError:
        raise errors.Unsupported(
            'gradebook_column_form did not originate from this session')
    if not gradebook_column_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    old_column = collection.find_one({'_id': gradebook_column_form._my_map[
        '_id']})
    if old_column['gradeSystemId'] != gradebook_column_form._my_map[
        'gradeSystemId']:
        if self._has_entries(gradebook_column_form.id_):
            raise errors.IllegalState(
                'Entries exist in this gradebook column. ' +
                'Cannot change the grade system.')
    collection.save(gradebook_column_form._my_map)
    self._forms[gradebook_column_form.get_id().get_identifier()] = UPDATED
    return objects.GradebookColumn(osid_object_map=gradebook_column_form.
        _my_map, runtime=self._runtime, proxy=self._proxy)