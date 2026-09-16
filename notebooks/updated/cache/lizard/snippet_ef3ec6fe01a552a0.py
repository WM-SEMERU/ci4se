def title(self, category):
    return sum([self.getWidth(category, x) for x in self.fields])