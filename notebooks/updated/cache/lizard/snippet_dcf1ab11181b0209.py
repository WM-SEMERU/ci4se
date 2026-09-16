def get_declared_items(self):
    d = self.declaration
    engine = d._d_engine
    if engine:
        layout = {}
        for k, h in engine._handlers.items():
            if not h.read_pair:
                continue
            v = getattr(d, k)
            if k in LAYOUT_KEYS:
                layout[k] = v
                continue
            yield k, v
        if layout:
            yield 'layout', layout