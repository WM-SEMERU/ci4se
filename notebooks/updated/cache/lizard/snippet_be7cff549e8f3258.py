def as_field_error(node, secid):
    assert node.name() == 'fieldExceptions'
    if node.isArray():
        return [XmlHelper.as_field_error(node.getValue(_), secid) for _ in
            range(node.numValues())]
    else:
        fld = XmlHelper.get_child_value(node, 'fieldId')
        info = node.getElement('errorInfo')
        src = XmlHelper.get_child_value(info, 'source')
        code = XmlHelper.get_child_value(info, 'code')
        cat = XmlHelper.get_child_value(info, 'category')
        msg = XmlHelper.get_child_value(info, 'message')
        subcat = XmlHelper.get_child_value(info, 'subcategory')
        return FieldError(security=secid, field=fld, source=src, code=code,
            category=cat, message=msg, subcategory=subcat)