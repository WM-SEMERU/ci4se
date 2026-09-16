def list_blocks(self):
    logger.debug('listing blocks')
    blocksList = BlocksList()
    result = self.library.Cli_ListBlocks(self.pointer, byref(blocksList))
    check_error(result, context='client')
    logger.debug('blocks: %s' % blocksList)
    return blocksList