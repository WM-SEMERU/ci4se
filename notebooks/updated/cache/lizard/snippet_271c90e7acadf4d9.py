def normalize(self):
    max_abs = max(self.table, key=abs)
    if max_abs == 0:
        raise ValueError("Can't normalize zeros")
    return self / max_abs