def xml(self):
    xml = self._get_xml(False)
    for key in self.impact_functions_fields:
        value = str(self.data(key))
        element = Element(key)
        element.text = value
        xml += tostring(element, 'unicode')
    xml += '</provenance_step>'
    return xml