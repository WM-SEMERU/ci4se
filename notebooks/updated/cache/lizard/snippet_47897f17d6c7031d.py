def _getOidLabel(self, nodeName, oidToLabelIdx, labelToOidIdx):
    if not nodeName:
        return nodeName, nodeName, ()
    if nodeName in labelToOidIdx:
        return labelToOidIdx[nodeName], nodeName, ()
    if nodeName in oidToLabelIdx:
        return nodeName, oidToLabelIdx[nodeName], ()
    if len(nodeName) < 2:
        return nodeName, nodeName, ()
    oid, label, suffix = self._getOidLabel(nodeName[:-1], oidToLabelIdx,
        labelToOidIdx)
    suffix = suffix + nodeName[-1:]
    resLabel = label + tuple([str(x) for x in suffix])
    if resLabel in labelToOidIdx:
        return labelToOidIdx[resLabel], resLabel, ()
    resOid = oid + suffix
    if resOid in oidToLabelIdx:
        return resOid, oidToLabelIdx[resOid], ()
    return oid, label, suffix