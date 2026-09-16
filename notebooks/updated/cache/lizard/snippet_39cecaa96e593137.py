def _check_len(self, pkt):
    if len(pkt) % 2:
        last_chr = pkt[-1]
        if last_chr <= b'\x80':
            return pkt[:-1] + b'\x00' + last_chr
        else:
            return pkt[:-1] + b'\xff' + chb(orb(last_chr) - 1)
    else:
        return pkt