def ListField(field):
    original_get_from_instance = field.get_from_instance

    def get_from_instance(self, instance):
        for value in original_get_from_instance(instance):
            yield value
    field.get_from_instance = MethodType(get_from_instance, field)
    return field