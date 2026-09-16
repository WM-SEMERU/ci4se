def pawns_at(self, x, y):
    for pawn in self.pawn.values():
        if pawn.collide_point(x, y):
            yield pawn