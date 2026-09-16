def _format_quantum(val, unit):
    q = quantity(val, unit)
    if q.canonical().get_unit() in ['rad', 's']:
        return quantity(val, 'm').formatted()[:-1] + unit
    else:
        return q.formatted()