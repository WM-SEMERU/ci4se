def get_filename_block_as_codepoints(self):
    codepoints = []
    codepoints += list(string2codepoint(self.filename.ljust(8, ' ')))
    codepoints.append(self.cfg.FTYPE_BASIC)
    codepoints.append(self.cfg.BASIC_ASCII)
    codepoints.append(self.gap_flag)
    if self.file_type != self.cfg.FTYPE_BASIC:
        codepoints = iter(codepoints)
        self.start_address = get_word(codepoints)
        log.info('machine code starting address: %s' % hex(self.start_address))
        self.load_address = get_word(codepoints)
        log.info('machine code loading address: %s' % hex(self.load_address))
    else:
        pass
    log.debug('filename block: %s' % pformat_codepoints(codepoints))
    return codepoints