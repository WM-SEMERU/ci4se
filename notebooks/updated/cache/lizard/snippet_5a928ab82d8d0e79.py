def hydrate(self, values):

    def hydrate_(obj):
        if isinstance(obj, Structure):
            try:
                f = self.hydration_functions[obj.tag]
            except KeyError:
                return obj
            else:
                return f(*map(hydrate_, obj.fields))
        elif isinstance(obj, list):
            return list(map(hydrate_, obj))
        elif isinstance(obj, dict):
            return {key: hydrate_(value) for key, value in obj.items()}
        else:
            return obj
    return tuple(map(hydrate_, values))