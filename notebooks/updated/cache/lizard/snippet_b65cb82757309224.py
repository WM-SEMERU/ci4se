def _parse_length(self, value, font_relative, callback, *args):
    if value.endswith('%'):
        frac = float(value[:-1]) / 100
        if font_relative:
            attrs = self._get_current_attributes()
            font_size = attrs.font.get_size() / pango.SCALE
            callback(frac * display_resolution * font_size, *args)
        else:
            alloc = self.textview.get_allocation()
            self.__parse_length_frac_size_allocate(self.textview, alloc,
                frac, callback, args)
            self.textview.connect('size-allocate', self.
                __parse_length_frac_size_allocate, frac, callback, args)
    elif value.endswith('pt'):
        callback(float(value[:-2]) * display_resolution, *args)
    elif value.endswith('em'):
        attrs = self._get_current_attributes()
        font_size = attrs.font.get_size() / pango.SCALE
        callback(float(value[:-2]) * display_resolution * font_size, *args)
    elif value.endswith('ex'):
        attrs = self._get_current_attributes()
        font_size = attrs.font.get_size() / pango.SCALE
        callback(float(value[:-2]) * display_resolution * font_size, *args)
    elif value.endswith('px'):
        callback(int(value[:-2]), *args)
    else:
        warnings.warn("Unable to parse length value '%s'" % value)