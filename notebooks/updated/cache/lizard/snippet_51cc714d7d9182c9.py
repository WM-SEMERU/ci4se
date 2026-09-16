def serializeGt(x, compress=True):
    assertType(x, GtElement)
    return _serialize(x, compress, librelic.gt_size_bin_abi, librelic.
        gt_write_bin_abi)