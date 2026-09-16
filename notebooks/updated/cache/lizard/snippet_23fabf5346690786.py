def single_valued(self, e):
    if self.state.mode == 'static':
        if type(e) in (int, bytes, float, bool):
            return True
        else:
            return e.cardinality <= 1
    else:
        return not self.symbolic(e)