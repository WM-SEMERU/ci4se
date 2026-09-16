def _SetField(self, args, type_info, value):
    if hasattr(type_info, 'enum'):
        try:
            coerced_obj = type_info.enum[value.upper()]
        except KeyError:
            coerced_obj = type_info.type.FromHumanReadable(value)
    else:
        coerced_obj = type_info.type.FromHumanReadable(value)
    args.Set(type_info.name, coerced_obj)