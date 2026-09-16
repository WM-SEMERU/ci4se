def load_blocks(self, location, blocks, ranges, query):
    if logging.getLogger().getEffectiveLevel() <= logging.DEBUG:
        msg = 'Loading {b.count} blocks from {loc}:{b.offset}+{b.length}'
        logging.debug(msg.format(b=blocks, loc=location))
    reader = self.blk_loader.load(location, blocks.offset, blocks.length)

    def decompress_block(range_):
        decomp = gzip_decompressor()
        buff = decomp.decompress(reader.read(range_))
        for line in BytesIO(buff):
            yield line

    def iter_blocks(reader):
        try:
            for r in ranges:
                yield decompress_block(r)
        finally:
            reader.close()
    iter_ = itertools.chain.from_iterable(iter_blocks(reader))
    iter_ = linearsearch(iter_, query.key)
    iter_ = itertools.takewhile(lambda line: line < query.end_key, iter_)
    return iter_