def get(self, center, target, date):
    if (center.index, target.index) in self.segments:
        pos, vel = self.segments[center.index, target.index
            ].compute_and_differentiate(date.jd)
        sign = 1
    else:
        pos, vel = self.segments[target.index, center.index
            ].compute_and_differentiate(date.jd)
        sign = -1
    if len(pos) == 3:
        pv = np.concatenate((pos, vel / S_PER_DAY))
    elif len(pos) == 6:
        pv = np.array(pos)
    else:
        raise JplError('Unknown state vector format')
    return sign * pv * 1000