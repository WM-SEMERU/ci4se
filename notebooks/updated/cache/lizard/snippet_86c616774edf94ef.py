def name_to_system_object(self, name):
    if isinstance(name, str):
        if self.allow_name_referencing:
            name = name
        else:
            raise NameError(
                'System.allow_name_referencing is set to False, cannot convert string to name'
                )
    elif isinstance(name, Object):
        name = str(name)
    return self.namespace.get(name, None)