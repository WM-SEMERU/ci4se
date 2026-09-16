def _update_refs(self, root, bearers, attribute, ref_text, xml_id):
    ref = ' #{} '.format(xml_id)
    for bearer in bearers:
        attribute_text = bearer.get(attribute).replace(ref_text, ref)
        refs = ' '.join(sorted(attribute_text.strip().split()))
        bearer.set(attribute, refs)