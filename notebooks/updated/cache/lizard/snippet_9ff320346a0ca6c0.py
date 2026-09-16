def advantage_as_result(self, move, val_scheme):
    test_board = cp(self)
    test_board.update(move)
    return test_board.material_advantage(move.color, val_scheme)