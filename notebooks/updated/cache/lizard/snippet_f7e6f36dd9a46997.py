def op_right(op):

    def method(self, other):
        return op(value_left(self, other), value_right(self, other))
    return method