def lookup_field_value(self, context, obj, field):
    curr_field = field.encode('ascii', 'ignore').decode('utf-8')
    if field.find('.') == -1:
        view_method = getattr(self, 'get_%s' % curr_field, None)
        if view_method:
            return view_method(obj)
    return self.lookup_obj_attribute(obj, field)