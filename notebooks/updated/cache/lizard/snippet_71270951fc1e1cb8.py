def split_blocks(text_block, w, cols, part_fmter=None):
    ts = []
    for line in text_block.splitlines():
        parts = []
        line = line.ljust(w, ' ')
        parts.append(line[:cols])
        scols = cols - 2
        parts.extend([(' ' + col(txt_block_cut, L, no_reset=1) + line[i:i +
            scols]) for i in range(cols, len(line), scols)])
        ts.append(parts)
    blocks = []
    for block_part_nr in xrange(len(ts[0])):
        tpart = []
        for lines_block in ts:
            tpart.append(lines_block[block_part_nr])
        if part_fmter:
            part_fmter(tpart)
        tpart[1] = col(tpart[1], H3)
        blocks.append('\n'.join(tpart))
    t = '\n'.join(blocks)
    return '\n%s\n' % t