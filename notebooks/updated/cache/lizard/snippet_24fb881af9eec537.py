def _get_subplot_extents(self, overlay, ranges, range_type):
    if range_type == 'combined':
        extents = {'extents': [], 'soft': [], 'hard': [], 'data': []}
    else:
        extents = {range_type: []}
    items = overlay.items()
    if self.batched and self.subplots:
        subplot = list(self.subplots.values())[0]
        subplots = [(k, subplot) for k in overlay.data.keys()]
    else:
        subplots = self.subplots.items()
    for key, subplot in subplots:
        found = False
        if subplot is None:
            continue
        layer = overlay.data.get(key, None)
        if isinstance(self.hmap, DynamicMap) and layer is None:
            for _, layer in items:
                if isinstance(layer, subplot.hmap.type):
                    found = True
                    break
            if not found:
                layer = None
        if layer is None or not subplot.apply_ranges:
            continue
        if isinstance(layer, CompositeOverlay):
            sp_ranges = ranges
        else:
            sp_ranges = util.match_spec(layer, ranges) if ranges else {}
        for rt in extents:
            extent = subplot.get_extents(layer, sp_ranges, range_type=rt)
            extents[rt].append(extent)
    return extents