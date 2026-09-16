def cons(self, i):
    if self.b[i] in 'aeiou':
        return False
    elif self.b[i] == 'y':
        return True if i == 0 else not self.cons(i - 1)
    return True