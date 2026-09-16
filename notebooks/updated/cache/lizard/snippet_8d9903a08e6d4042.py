def orientality(self):
    sun = self.chart.getObject(const.SUN)
    return orientality(self.obj, sun)