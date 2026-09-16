def _parse_block_postheader(line):
    parts = line[1:].split(')', 1)
    qlen = int(parts[0])
    if not len(parts[1]) == qlen:
        logging.warn('postheader expected %d-long query, found %d', qlen,
            len(parts[1]))
    return qlen, parts[1]