def get_block_info(self, blocktype, db_number):
    blocktype = snap7.snap7types.block_types.get(blocktype)
    if not blocktype:
        raise Snap7Exception('The blocktype parameter was invalid')
    logger.debug('retrieving block info for block %s of type %s' % (
        db_number, blocktype))
    data = TS7BlockInfo()
    result = self.library.Cli_GetAgBlockInfo(self.pointer, blocktype,
        db_number, byref(data))
    check_error(result, context='client')
    return data