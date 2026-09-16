def _generate_ascii(self, matrix, foreground, background):
    return '\n'.join([''.join([(foreground if cell else background) for
        cell in row]) for row in matrix])