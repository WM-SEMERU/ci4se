def get_default(self, node):
    if node.inst.properties.get('woset', False):
        return rdltypes.OnWriteType.woset
    elif node.inst.properties.get('woclr', False):
        return rdltypes.OnWriteType.woclr
    else:
        return self.default