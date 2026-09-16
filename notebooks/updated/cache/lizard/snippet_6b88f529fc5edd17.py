def hms(segundos):
    h = segundos / 3600
    m = (segundos - 3600 * h) / 60
    s = segundos - 3600 * h - m * 60
    return h, m, s