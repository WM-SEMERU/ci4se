def _empty_not_in_check(self, position, direction):

    def valid_square(square):
        return position.is_square_empty(square) and not self.in_check(position,
            square)
    return valid_square(direction(self.location, 1)) and valid_square(direction
        (self.location, 2))