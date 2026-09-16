def read_header_at(cls, f):
    header_parser = BlockHeaderSerializer()
    hdr = header_parser.deserialize(f)
    h = {}
    h['version'] = hdr.version
    h['prev_block_hash'] = '%064x' % hdr.prev_block
    h['merkle_root'] = '%064x' % hdr.merkle_root
    h['timestamp'] = hdr.timestamp
    h['bits'] = hdr.bits
    h['nonce'] = hdr.nonce
    h['hash'] = hdr.calculate_hash()
    return h