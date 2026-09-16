def deserialize(self, obj, encoders=None, embedded=False, create_instance=True
    ):
    if not encoders:
        encoders = []
    for encoder in (encoders + self.standard_encoders):
        obj = encoder.decode(obj)
    if isinstance(obj, dict):
        if create_instance and '__collection__' in obj and obj['__collection__'
            ] in self.collections and 'pk' in obj:
            attributes = copy.deepcopy(obj)
            del attributes['__collection__']
            if '__ref__' in attributes:
                del attributes['__ref__']
            if '__lazy__' in attributes:
                lazy = attributes['__lazy__']
                del attributes['__lazy__']
            else:
                lazy = True
            output_obj = self.create_instance(obj['__collection__'],
                attributes, lazy=lazy)
        else:
            output_obj = {}
            for key, value in obj.items():
                output_obj[key] = self.deserialize(value, encoders=encoders)
    elif isinstance(obj, (list, tuple)):
        output_obj = list(map(lambda x: self.deserialize(x), obj))
    else:
        output_obj = obj
    return output_obj