def check_move(self, move_type, move_x, move_y):
    if move_type not in self.move_types:
        raise ValueError('This is not a valid move!')
    if move_x < 0 or move_x >= self.board_width:
        raise ValueError('This is not a valid X position of the move!')
    if move_y < 0 or move_y >= self.board_height:
        raise ValueError('This is not a valid Y position of the move!')
    move_des = {}
    move_des['move_type'] = move_type
    move_des['move_x'] = move_x
    move_des['move_y'] = move_y
    self.num_moves += 1
    return move_des