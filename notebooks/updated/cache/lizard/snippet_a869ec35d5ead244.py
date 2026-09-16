def API520_B(Pset, Pback, overpressure=0.1):
    r
    gauge_backpressure = (Pback - atm) / (Pset - atm) * 100
    if overpressure not in [0.1, 0.16, 0.21]:
        raise Exception('Only overpressure of 10%, 16%, or 21% are permitted')
    if (overpressure == 0.1 and gauge_backpressure < 30 or overpressure == 
        0.16 and gauge_backpressure < 38 or overpressure == 0.21 and 
        gauge_backpressure < 50):
        return 1
    elif gauge_backpressure > 50:
        raise Exception('Gauge pressure must be < 50%')
    if overpressure == 0.16:
        Kb = interp(gauge_backpressure, Kb_16_over_x, Kb_16_over_y)
    elif overpressure == 0.1:
        Kb = interp(gauge_backpressure, Kb_10_over_x, Kb_10_over_y)
    return Kb