def move_to_collection(self, request, *args, **kwargs):
    ids = self.get_ids(request.data)
    src_collection_id = self.get_id(request.data, 'source_collection')
    dst_collection_id = self.get_id(request.data, 'destination_collection')
    src_collection = self._get_collection_for_user(src_collection_id,
        request.user)
    dst_collection = self._get_collection_for_user(dst_collection_id,
        request.user)
    entity_qs = self._get_entities(request.user, ids)
    entity_qs.move_to_collection(src_collection, dst_collection)
    return Response()