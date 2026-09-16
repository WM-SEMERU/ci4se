def find_in_history(self, tocursor, start_idx, backward):
    if start_idx is None:
        start_idx = len(self.history)
    step = -1 if backward else 1
    idx = start_idx
    if len(tocursor) == 0 or self.hist_wholeline:
        idx += step
        if idx >= len(self.history) or len(self.history) == 0:
            return '', len(self.history)
        elif idx < 0:
            idx = 0
        self.hist_wholeline = True
        return self.history[idx], idx
    else:
        for index in range(len(self.history)):
            idx = (start_idx + step * (index + 1)) % len(self.history)
            entry = self.history[idx]
            if entry.startswith(tocursor):
                return entry[len(tocursor):], idx
        else:
            return None, start_idx