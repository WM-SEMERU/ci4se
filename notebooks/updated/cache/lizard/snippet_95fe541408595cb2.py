def __get_total_angle(self, angle, pos):
    tot_angle = angle - self.branches[pos][1]
    if self.sigma[1] != 0:
        tot_angle += gauss(0, self.sigma[1]) * pi
    return tot_angle