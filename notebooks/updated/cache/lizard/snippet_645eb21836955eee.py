def get_object_collection(self, object_name=''):
    object_names = self.get_object(object_name).get_objects()
    return {obj: self.get_object(obj) for obj in object_names}