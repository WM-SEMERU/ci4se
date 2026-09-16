def add_template(template, **kwargs):
    tmpl = Template()
    tmpl.name = template.name
    if template.description:
        tmpl.description = template.description
    if template.layout:
        tmpl.layout = get_layout_as_string(template.layout)
    db.DBSession.add(tmpl)
    if template.templatetypes is not None:
        types = template.templatetypes
        for templatetype in types:
            ttype = _update_templatetype(templatetype)
            tmpl.templatetypes.append(ttype)
    db.DBSession.flush()
    return tmpl