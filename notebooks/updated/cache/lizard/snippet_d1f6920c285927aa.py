def CSS_setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
    assert isinstance(propertyName, (str,)
        ), "Argument 'propertyName' must be of type '['str']'. Received type: '%s'" % type(
        propertyName)
    assert isinstance(value, (str,)
        ), "Argument 'value' must be of type '['str']'. Received type: '%s'" % type(
        value)
    subdom_funcs = self.synchronous_command(
        'CSS.setEffectivePropertyValueForNode', nodeId=nodeId, propertyName
        =propertyName, value=value)
    return subdom_funcs