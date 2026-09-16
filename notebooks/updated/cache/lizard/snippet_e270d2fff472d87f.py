def create_authorization(self, authorization_form):
    collection = JSONClientValidated('authorization', collection=
        'Authorization', runtime=self._runtime)
    if not isinstance(authorization_form, ABCAuthorizationForm):
        raise errors.InvalidArgument(
            'argument type is not an AuthorizationForm')
    if authorization_form.is_for_update():
        raise errors.InvalidArgument(
            'the AuthorizationForm is for update only, not create')
    try:
        if self._forms[authorization_form.get_id().get_identifier()
            ] == CREATED:
            raise errors.IllegalState(
                'authorization_form already used in a create transaction')
    except KeyError:
        raise errors.Unsupported(
            'authorization_form did not originate from this session')
    if not authorization_form.is_valid():
        raise errors.InvalidArgument(
            'one or more of the form elements is invalid')
    try:
        osid_map = collection.find_one({'agentId': authorization_form.
            _my_map['agentId'], 'functionId': authorization_form._my_map[
            'functionId'], 'qualifierId': authorization_form._my_map[
            'qualifierId'], 'assignedVaultIds': authorization_form._my_map[
            'assignedVaultIds']})
        osid_map['startDate'] = authorization_form._my_map['startDate']
        osid_map['endDate'] = authorization_form._my_map['endDate']
        collection.save(osid_map)
    except errors.NotFound:
        insert_result = collection.insert_one(authorization_form._my_map)
        self._forms[authorization_form.get_id().get_identifier()] = CREATED
        osid_map = collection.find_one({'_id': insert_result.inserted_id})
    result = objects.Authorization(osid_object_map=osid_map, runtime=self.
        _runtime, proxy=self._proxy)
    return result