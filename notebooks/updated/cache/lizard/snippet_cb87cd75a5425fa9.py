def appendAnchor(self, name=None, position=None, color=None, anchor=None):
    identifier = None
    if anchor is not None:
        anchor = normalizers.normalizeAnchor(anchor)
        if name is None:
            name = anchor.name
        if position is None:
            position = anchor.position
        if color is None:
            color = anchor.color
        if anchor.identifier is not None:
            existing = set([a.identifier for a in self.anchors if a.
                identifier is not None])
            if anchor.identifier not in existing:
                identifier = anchor.identifier
    name = normalizers.normalizeAnchorName(name)
    position = normalizers.normalizeCoordinateTuple(position)
    if color is not None:
        color = normalizers.normalizeColor(color)
    identifier = normalizers.normalizeIdentifier(identifier)
    return self._appendAnchor(name, position=position, color=color,
        identifier=identifier)