def customwarn(message, category, filename, lineno, *args, **kwargs):
    if category is PsyPlotWarning:
        logger.warning(warnings.formatwarning('\n%s' % message, category,
            filename, lineno))
    elif category is PsyPlotCritical:
        logger.critical(warnings.formatwarning('\n%s' % message, category,
            filename, lineno), exc_info=True)
    else:
        old_showwarning(message, category, filename, lineno, *args, **kwargs)