def append_index(self, num_rows):
    width = len(str(num_rows - 1))

    def f(datum):
        return str(datum.idx).ljust(width)
    header = ' ' * width
    self.append(header, f)