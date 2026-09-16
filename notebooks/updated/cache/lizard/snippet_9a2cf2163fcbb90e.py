def GetWSAActionOutput(operation):
    attr = operation.output.action
    if attr is not None:
        return attr
    targetNamespace = operation.getPortType().getTargetNamespace()
    ptName = operation.getPortType().name
    msgName = operation.output.name
    if not msgName:
        msgName = operation.name + 'Response'
    if targetNamespace.endswith('/'):
        return '%s%s/%s' % (targetNamespace, ptName, msgName)
    return '%s/%s/%s' % (targetNamespace, ptName, msgName)