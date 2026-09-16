def get_top(self, stat, n):
    return sorted(self.stats, key=lambda x: getattr(x, stat), reverse=True)[:n]