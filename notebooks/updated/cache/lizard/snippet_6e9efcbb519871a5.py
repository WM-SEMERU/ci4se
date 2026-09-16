def rar3_type(btype):
    if btype < rf.RAR_BLOCK_MARK or btype > rf.RAR_BLOCK_ENDARC:
        return '*UNKNOWN*'
    return block_strs[btype - rf.RAR_BLOCK_MARK]