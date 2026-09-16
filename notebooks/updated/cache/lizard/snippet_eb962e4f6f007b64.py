def sr(self, multi=0):
    remain = self.res[:]
    sr = []
    i = 0
    while i < len(remain):
        s = remain[i]
        j = i
        while j < len(remain) - 1:
            j += 1
            r = remain[j]
            if r.answers(s):
                sr.append((s, r))
                if multi:
                    remain[i]._answered = 1
                    remain[j]._answered = 2
                    continue
                del remain[j]
                del remain[i]
                i -= 1
                break
        i += 1
    if multi:
        remain = [x for x in remain if not hasattr(x, '_answered')]
    return SndRcvList(sr), PacketList(remain)