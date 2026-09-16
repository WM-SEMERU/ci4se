def add(self, *number):
    return self._format_result(sum([int(n) for n in number]))