def in_miso_and_inner(self):
    return len(self.successor) == 1 and self.successor[0
        ] is not None and not self.successor[0].in_or_out and len(self.
        precedence) > 1 and self.precedence[0
        ] is not None and not self.successor[0].in_or_out