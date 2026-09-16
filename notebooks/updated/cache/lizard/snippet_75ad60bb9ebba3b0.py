def gauge_from_t(t, SI=True, schedule='BWG'):
    r
    tol = 0.1
    if SI:
        t_inch = round(t / inch, 9)
    else:
        t_inch = t
    try:
        sch_integers, sch_inch, sch_SI, decreasing = wire_schedules[schedule]
    except:
        raise ValueError('Wire gauge schedule not found')
    sch_max, sch_min = sch_inch[0], sch_inch[-1]
    if t_inch > sch_max:
        raise ValueError(
            'Input thickness is above the largest in the selected schedule')
    if t_inch in sch_inch:
        gauge = sch_integers[sch_inch.index(t_inch)]
    else:
        for i in range(len(sch_inch)):
            if sch_inch[i] >= t_inch:
                larger = sch_inch[i]
            else:
                break
        if larger == sch_min:
            gauge = sch_min
        else:
            smaller = sch_inch[i]
            if t_inch - smaller <= tol * (larger - smaller):
                gauge = sch_integers[i]
            else:
                gauge = sch_integers[i - 1]
    return gauge