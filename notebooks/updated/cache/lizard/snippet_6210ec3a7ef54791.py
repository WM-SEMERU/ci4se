def CreateFlowArgs(self, flow_name=None):
    if not self._flow_descriptors:
        self._flow_descriptors = {}
        result = self._context.SendRequest('ListFlowDescriptors', None)
        for item in result.items:
            self._flow_descriptors[item.name] = item
    try:
        flow_descriptor = self._flow_descriptors[flow_name]
    except KeyError:
        raise UnknownFlowName(flow_name)
    return utils.CopyProto(utils.UnpackAny(flow_descriptor.default_args))