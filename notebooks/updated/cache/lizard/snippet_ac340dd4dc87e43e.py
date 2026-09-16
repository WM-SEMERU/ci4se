def _sampleLocationOnDisc(self, top=None):
    if top is None:
        z = random.choice([-1, 1]) * self.height / 2.0
    else:
        z = self.height / 2.0 if top else -self.height / 2.0
    sampledAngle = 2 * random.random() * pi
    sampledRadius = self.radius * sqrt(random.random())
    x, y = sampledRadius * cos(sampledAngle), sampledRadius * sin(sampledAngle)
    return [x, y, z]