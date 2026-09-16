def _next_move_direction(self):
    nmoves = len(self.moves)
    move = np.random.randint(1, nmoves + 1)
    while self.prev_move == (move + 3) % nmoves:
        move = np.random.randint(1, nmoves + 1)
    self.prev_move = move
    return np.array(self.moves[move])