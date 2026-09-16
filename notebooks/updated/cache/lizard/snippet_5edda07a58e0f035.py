def matchstartorient(self, seq, factor=0.7):
    ans = []
    txts, endpoints, scores = self.scan(seq, factor=factor)
    for txt, startstop in zip(txts, endpoints):
        start, stop = startstop
        rctxt = revcomplement(txt)
        orient = self.bestscore(txt, 1) >= self.bestscore(rctxt, 1)
        ans.append((start, orient))
    return ans