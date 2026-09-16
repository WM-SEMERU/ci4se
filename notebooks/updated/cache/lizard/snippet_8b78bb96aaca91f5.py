def resource_etree_element(self, resource, element_name='url'):
    e = Element(element_name)
    sub = Element('loc')
    sub.text = resource.uri
    e.append(sub)
    if resource.timestamp is not None:
        sub = Element('lastmod')
        sub.text = str(resource.lastmod)
        e.append(sub)
    md_atts = {}
    for att in ('capability', 'change', 'hash', 'length', 'path',
        'mime_type', 'md_at', 'md_completed', 'md_from', 'md_until'):
        val = getattr(resource, att, None)
        if val is not None:
            md_atts[self._xml_att_name(att)] = str(val)
    if len(md_atts) > 0:
        md = Element('rs:md', md_atts)
        e.append(md)
    if hasattr(resource, 'ln') and resource.ln is not None:
        for ln in resource.ln:
            self.add_element_with_atts_to_etree(e, 'rs:ln', ln)
    if self.pretty_xml:
        e.tail = '\n'
    return e