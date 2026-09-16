def delete_activity(self, activity_id=None):
    if activity_id is None:
        raise NullArgument()
    if not isinstance(activity_id, Id):
        raise InvalidArgument('argument type is not an osid Id')
    url_path = construct_url('activities', bank_id=self._catalog_idstr,
        act_id=activity_id)
    result = self._delete_request(url_path)
    return objects.Activity(result)