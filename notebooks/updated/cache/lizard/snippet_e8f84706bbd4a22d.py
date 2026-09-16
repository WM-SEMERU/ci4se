def update_log_entry(self, log_entry_form):
    collection = JSONClientValidated('logging', collection='LogEntry',
        runtime=self._runtime)
    if not isinstance(log_entry_form, ABCLogEntryForm):
        raise errors.InvalidArgument('argument type is not an LogEntryForm')
    if not log_entry_form.is_for_update():
        raise errors.InvalidArgument(
            'the LogEntryForm is for update only, not create')
    try:
        if self._forms[log_entry_form.get_id().get_identifier()] == UPDATED:
            raise errors.IllegalState(
                'log_entry_form already used in an update transaction')
    except KeyError:
        raise errors.Unsupported(
            'log_entry_form did not originate from this session')
    if not log_entry_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    collection.save(log_entry_form._my_map)
    self._forms[log_entry_form.get_id().get_identifier()] = UPDATED
    return objects.LogEntry(osid_object_map=log_entry_form._my_map, runtime
        =self._runtime, proxy=self._proxy)