def to_dict(self):
    return {'type': self.__class__.__name__, 'points': self.points.tolist(),
        'knots': self.knots.tolist(), 'closed': self.closed}