def _attribute_definition(self, attrid):
    attrs = self._schema['attributes']
    try:
        return dict(attrs[attrid])
    except KeyError:
        attr_names = self._schema['attribute_names']
        attrdef = attrs.get(attr_names.get(str(attrid).lower()))
        if not attrdef:
            return None
        else:
            return dict(attrdef)