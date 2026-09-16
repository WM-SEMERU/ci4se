def set_attribute_xsi_type(self, el, **kw):
    if kw.get('typed', self.typed):
        namespaceURI, typeName = kw.get('type', _get_xsitype(self))
        if namespaceURI and typeName:
            self.logger.debug('attribute: (%s, %s)', namespaceURI, typeName)
            el.setAttributeType(namespaceURI, typeName)