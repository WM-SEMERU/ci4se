def _create_text_node(self, root, name, value, cdata=False):
    if is_empty_or_none(value):
        return
    if type(value) == date:
        value = date_to_string(value)
    if type(value) == datetime:
        value = datetime_to_string(value)
    if isinstance(value, Decimal):
        value = '0' if not value else str(value)
    tag = root.ownerDocument.createElement(name)
    value = value.decode('utf-8')
    if cdata:
        tag.appendChild(root.ownerDocument.createCDATASection(value))
    else:
        tag.appendChild(root.ownerDocument.createTextNode(value))
    return root.appendChild(tag)