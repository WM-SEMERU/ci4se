def sequence(self):
    if len(self.Points[0]) == 2:
        if self.Sort == 'X' or self.Sort == 'x':
            self.Points.sort(key=lambda x: x[0])
            self.order(self.Points)
        elif self.Sort == 'Y' or self.Sort == 'y':
            self.Points.sort(key=lambda x: x[1])
            self.order(self.Points)
        else:
            self.order(self.Points)
    if len(self.Points[0]) == 3:
        if self.Sort == 'X' or self.Sort == 'x':
            self.Points.sort(key=lambda x: x[0])
            self.order(self.Points)
        elif self.Sort == 'Y' or self.Sort == 'y':
            self.Points.sort(key=lambda x: x[1])
            self.order(self.Points)
        elif self.Sort == 'Z' or self.Sort == 'Z':
            self.Points.sort(key=lambda x: x[2])
            self.order(self.Points)
        else:
            self.order(self.Points)