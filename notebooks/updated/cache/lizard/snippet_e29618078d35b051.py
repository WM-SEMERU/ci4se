def get_input_widget(self, fieldname, arnum=0, **kw):
    context = self.get_ar()
    schema = context.Schema()
    base_fieldname = fieldname.split('-')[0]
    field = context.getField(base_fieldname)
    new_fieldname = self.get_fieldname(field, arnum)
    new_field = field.copy(name=new_fieldname)
    fieldvalues = self.fieldvalues
    field_value = fieldvalues.get(new_fieldname)
    value = field_value

    def getAccessor(instance):

        def accessor(**kw):
            return value
        return accessor
    kw['here'] = context
    kw['context'] = context
    kw['fieldName'] = new_fieldname
    schema._fields[new_fieldname] = new_field
    new_field.getAccessor = getAccessor
    form = dict()
    form[new_fieldname] = value
    self.request.form.update(form)
    logger.info(
        'get_input_widget: fieldname={} arnum={} -> new_fieldname={} value={}'
        .format(fieldname, arnum, new_fieldname, value))
    widget = context.widget(new_fieldname, **kw)
    return widget