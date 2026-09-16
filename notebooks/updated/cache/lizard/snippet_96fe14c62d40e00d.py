def contains(self, p):
    inside = False
    if p in self.bounds():
        for s in self.segments():
            if (s.p.y > p.y) != (s.q.y > p.y) and p.x < (s.q.x - s.p.x) * (p
                .y - s.p.y) / (s.q.y - s.p.y) + s.p.x:
                inside = not inside
    return inside