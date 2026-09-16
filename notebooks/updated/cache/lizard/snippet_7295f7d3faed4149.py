def delete_asset(self, asset_id=None):
    if asset_id is None:
        raise NullArgument()
    if not isinstance(asset_id, Id):
        raise InvalidArgument('argument type is not an osid Id')
    url_path = construct_url('assets', bank_id=self._catalog_idstr,
        asset_id=asset_id)
    result = self._delete_request(url_path)
    return objects.Asset(result)