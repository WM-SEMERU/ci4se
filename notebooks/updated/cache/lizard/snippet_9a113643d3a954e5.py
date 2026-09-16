def do_IHaveRequest(self, apdu):
    if _debug:
        WhoHasIHaveServices._debug('do_IHaveRequest %r', apdu)
    if apdu.deviceIdentifier is None:
        raise MissingRequiredParameter('deviceIdentifier required')
    if apdu.objectIdentifier is None:
        raise MissingRequiredParameter('objectIdentifier required')
    if apdu.objectName is None:
        raise MissingRequiredParameter('objectName required')