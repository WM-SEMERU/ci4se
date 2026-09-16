def get_preferred_object(self, resource, object_type, content_id, location=0):
    collection = self.get_object(resource=resource, object_type=object_type,
        content_ids=content_id, object_ids='0', location=location)
    return collection[0]