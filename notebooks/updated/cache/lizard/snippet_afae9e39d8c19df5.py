def _validate_namespace(self, namespace):
    if namespace not in self.namespaces:
        raise CIMError(CIM_ERR_INVALID_NAMESPACE, _format(
            'Namespace does not exist in mock repository: {0!A}', namespace))