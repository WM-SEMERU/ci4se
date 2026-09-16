def suggest(self, w):
    if len(self) == 0:
        self.load()
    if len(w) == 1:
        return [(w, 1.0)]
    if w in PUNCTUATION:
        return [(w, 1.0)]
    if w.replace('.', '').isdigit():
        return [(w, 1.0)]
    candidates = self._known([w]) or self._known(self._edit1(w)
        ) or self._known(self._edit2(w)) or [w]
    candidates = [(self.get(c, 0.0), c) for c in candidates]
    s = float(sum(p for p, w in candidates) or 1)
    candidates = sorted(((p / s, w) for p, w in candidates), reverse=True)
    candidates = [(w.istitle() and x.title() or x, p) for p, x in candidates]
    return candidates