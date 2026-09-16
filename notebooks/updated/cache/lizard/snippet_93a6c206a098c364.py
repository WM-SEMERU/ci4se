def DiamReq(cmd, **fields):
    upfields, name = getCmdParams(cmd, True, **fields)
    p = DiamG(**upfields)
    p.name = name
    return p