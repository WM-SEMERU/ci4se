def _create_dict(self, format, args):
    builder = None
    if args is None or not args[0]:
        rest_format = self._create(format[2:], None)[1]
        rest_format = self._create(rest_format, None)[1]
        if not rest_format.startswith('}'):
            raise TypeError('dictionary type string not closed with }')
        rest_format = rest_format[1:]
        element_type = format[:len(format) - len(rest_format)]
        builder = GLib.VariantBuilder.new(variant_type_from_string(
            element_type))
    else:
        builder = GLib.VariantBuilder.new(variant_type_from_string('a{?*}'))
        for k, v in args[0].items():
            key_v, rest_format, _ = self._create(format[2:], [k])
            val_v, rest_format, _ = self._create(rest_format, [v])
            if not rest_format.startswith('}'):
                raise TypeError('dictionary type string not closed with }')
            rest_format = rest_format[1:]
            entry = GLib.VariantBuilder.new(variant_type_from_string('{?*}'))
            entry.add_value(key_v)
            entry.add_value(val_v)
            builder.add_value(entry.end())
    if args is not None:
        args = args[1:]
    return builder.end(), rest_format, args