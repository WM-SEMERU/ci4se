def add(self, func, position):
    try:
        if self.loc_adjacent_to_opponent_king(func(self.location), position):
            return
    except IndexError:
        return
    if position.is_square_empty(func(self.location)):
        yield self.create_move(func(self.location), notation_const.MOVEMENT)
    elif position.piece_at_square(func(self.location)).color != self.color:
        yield self.create_move(func(self.location), notation_const.CAPTURE)