def _get_philny(self, C, mag):
    if mag <= 4.5:
        return C['phi1']
    elif mag >= 5.5:
        return C['phi2']
    else:
        return C['phi2'] + (C['phi1'] - C['phi2']) * (5.5 - mag)