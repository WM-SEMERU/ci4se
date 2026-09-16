def create_item(self, item_form):
    collection = JSONClientValidated('assessment', collection='Item',
        runtime=self._runtime)
    if not isinstance(item_form, ABCItemForm):
        raise errors.InvalidArgument('argument type is not an ItemForm')
    if item_form.is_for_update():
        raise errors.InvalidArgument(
            'the ItemForm is for update only, not create')
    try:
        if self._forms[item_form.get_id().get_identifier()] == CREATED:
            raise errors.IllegalState(
                'item_form already used in a create transaction')
    except KeyError:
        raise errors.Unsupported(
            'item_form did not originate from this session')
    if not item_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    insert_result = collection.insert_one(item_form._my_map)
    self._forms[item_form.get_id().get_identifier()] = CREATED
    result = objects.Item(osid_object_map=collection.find_one({'_id':
        insert_result.inserted_id}), runtime=self._runtime, proxy=self._proxy)
    return result