def disable_warnings(critical=False):
    warnings.filterwarnings('ignore', '\\w', PsyPlotWarning, 'psyplot', 0)
    if critical:
        warnings.filterwarnings('ignore', '\\w', PsyPlotCritical, 'psyplot', 0)