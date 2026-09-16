def convert_column(self, values):
    assert all(values >= 0), 'Cannot normalize a column with negatives'
    total = sum(values)
    if total > 0:
        return values / total
    else:
        return values