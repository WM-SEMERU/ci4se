def _get_style_of_faulting_term(self, C, rup):
    if np.abs(rup.rake) <= 30.0 or 180.0 - np.abs(rup.rake) <= 30.0:
        return C['e1']
    elif rup.rake > 30.0 and rup.rake < 150.0:
        return C['e3']
    else:
        return C['e2']