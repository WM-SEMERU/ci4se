def add_watch_point(self, string, rating, importance=5):
    d = {}
    d['string'] = string
    d['rating'] = rating
    d['importance'] = importance
    self.watch_points.append(d)