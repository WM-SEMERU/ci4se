def _merge_ovls(self, ovls):
    ret = reduce(lambda x, y: x.merge(y), ovls)
    ret.value = self.value(ovls=ovls)
    ret.set_props(self.props)
    return ret