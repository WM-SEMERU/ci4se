def append_rally_point(self, p):
    if self.rally_count() > 9:
        print("Can't have more than 10 rally points, not adding.")
        return
    self.rally_points.append(p)
    self.reindex()