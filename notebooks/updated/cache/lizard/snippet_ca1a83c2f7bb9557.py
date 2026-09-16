def _getNodeData(self, name, metadata, channel=None):
    nodeChannel = None
    if name in metadata:
        nodeChannelList = metadata[name]
        if len(nodeChannelList) > 1:
            nodeChannel = channel if channel is not None else nodeChannelList[0
                ]
        elif len(nodeChannelList) == 1:
            nodeChannel = nodeChannelList[0]
        else:
            LOG.warning(
                'HMDevice._getNodeData: %s not found in %s, empty nodeChannelList'
                 % (name, metadata))
            return None
        if nodeChannel is not None and nodeChannel in self.CHANNELS:
            return self._hmchannels[nodeChannel].getValue(name)
    LOG.error('HMDevice._getNodeData: %s not found in %s' % (name, metadata))
    return None