def map2hosts(hostmap):
    ret = hostmap[0].copy()
    for net, mask in hostmap[1]:
        ret.add('%s/%d' % (num2dq(net), mask2netmask(mask)))
    return ret