def process_request(self, request_object):
    entity = request_object.entity_cls.get(request_object.identifier)
    entity.delete()
    return ResponseSuccessWithNoContent()