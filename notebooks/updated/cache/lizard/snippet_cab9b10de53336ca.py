def classify_coupling(coupling):
    lower, upper = coupling
    if lower is None and upper is None:
        return CouplingClass.Uncoupled
    elif lower is None or upper is None:
        return CouplingClass.DirectionalReverse
    elif lower == 0.0 and upper == 0.0:
        return CouplingClass.Inconsistent
    elif lower <= 0.0 and upper >= 0.0:
        return CouplingClass.DirectionalForward
    elif abs(lower - upper) < 1e-06:
        return CouplingClass.Full
    else:
        return CouplingClass.Partial