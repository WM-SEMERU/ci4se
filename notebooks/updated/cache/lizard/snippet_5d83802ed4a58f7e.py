def kappa_analysis_altman(kappa):
    try:
        if kappa < 0.2:
            return 'Poor'
        if kappa >= 0.2 and kappa < 0.4:
            return 'Fair'
        if kappa >= 0.4 and kappa < 0.6:
            return 'Moderate'
        if kappa >= 0.6 and kappa < 0.8:
            return 'Good'
        if kappa >= 0.8 and kappa <= 1:
            return 'Very Good'
        return 'None'
    except Exception:
        return 'None'