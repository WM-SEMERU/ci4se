def remove_asset(self, asset_id, composition_id):
    if not isinstance(composition_id, ABCId
        ) and composition_id.get_identifier_namespace(
        ) != 'repository.Composition':
        raise errors.InvalidArgument('the argument is not a valid OSID Id')
    composition_map, collection = self._get_composition_collection(
        composition_id)
    try:
        composition_map['assetIds'].remove(str(asset_id))
    except (KeyError, ValueError):
        raise errors.NotFound()
    collection.save(composition_map)