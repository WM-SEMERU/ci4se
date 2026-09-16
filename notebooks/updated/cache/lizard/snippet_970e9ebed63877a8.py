def addCluster(self, cx, cy, item, count, lam_percent=0.25):
    dx, dy = map(lambda v: v * lam_percent, self.psize)
    total = 0
    while total < count:
        points = np.random.poisson(lam=(dx, dy), size=(count, 2))
        for x, y in points:
            px, py = int(x - dx + cx), int(y - dy + cy)
            if self.getPatch(px, py) is None:
                self.setPatch(px, py, item)
                total += 1
                if total == count:
                    break