def get_median_area(self, mag, rake):
    if rake is None:
        return power(10.0, mag - 4.185)
    elif -45 <= rake <= 45 or rake >= 135 or rake <= -135:
        return power(10.0, mag - 4.18)
    else:
        return power(10.0, mag - 4.19)