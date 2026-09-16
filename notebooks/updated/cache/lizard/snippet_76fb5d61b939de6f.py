def getattr(self, name, context=None, class_context=True):
    values = self.locals.get(name, [])
    if name in self.special_attributes and class_context and not values:
        result = [self.special_attributes.lookup(name)]
        if name == '__bases__':
            result += values
        return result
    values = list(values)
    for classnode in self.ancestors(recurs=True, context=context):
        values += classnode.locals.get(name, [])
    if class_context:
        values += self._metaclass_lookup_attribute(name, context)
    if not values:
        raise exceptions.AttributeInferenceError(target=self, attribute=
            name, context=context)
    for value in values:
        if isinstance(value, node_classes.AssignName):
            stmt = value.statement()
            if isinstance(stmt, node_classes.AnnAssign) and stmt.value is None:
                raise exceptions.AttributeInferenceError(target=self,
                    attribute=name, context=context)
    return values