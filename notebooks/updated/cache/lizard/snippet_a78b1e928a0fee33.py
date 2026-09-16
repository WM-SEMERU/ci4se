def create_xml(self, useNamespace=False):
    UNTL_NAMESPACE = 'http://digital2.library.unt.edu/untl/'
    UNTL = '{%s}' % UNTL_NAMESPACE
    NSMAP = {'untl': UNTL_NAMESPACE}
    if useNamespace:
        root = Element(UNTL + self.tag, nsmap=NSMAP)
    else:
        root = Element(self.tag)
    self.sort_untl(UNTL_XML_ORDER)
    for element in self.children:
        if useNamespace:
            create_untl_xml_subelement(root, element, UNTL)
        else:
            create_untl_xml_subelement(root, element)
    return root