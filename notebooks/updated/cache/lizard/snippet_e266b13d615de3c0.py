def check_ordered(self):
    sys.stderr.write('error unimplemented check_ordered\n')
    sys.exit()
    seen_chrs = set()
    curr_chr = None
    prevstart = 0
    for l in self._lines:
        if not l['rng']:
            continue
        if l['rng'].chr != curr_chr:
            prevstart = 0
            if l['rng'].chr in seen_chrs:
                return False
            curr_chr = l['rng'].chr
            seen_chrs.add(curr_chr)
        if l['rng'].start < prevstart:
            return False
        prevstart = l['rng'].start
    return True