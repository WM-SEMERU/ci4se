def in_single_path(self):
    return len(self.successor) == 1 and not self.successor[0
        ].in_or_out and len(self.precedence) == 1 and len(self.precedence[0
        ].successor) <= 1