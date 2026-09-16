def sortJobs(jobTypes, options):
    longforms = {'med': 'median', 'ave': 'average', 'min': 'min', 'total':
        'total', 'max': 'max'}
    sortField = longforms[options.sortField]
    if (options.sortCategory == 'time' or options.sortCategory == 'clock' or
        options.sortCategory == 'wait' or options.sortCategory == 'memory'):
        return sorted(jobTypes, key=lambda tag: getattr(tag, '%s_%s' % (
            sortField, options.sortCategory)), reverse=options.sortReverse)
    elif options.sortCategory == 'alpha':
        return sorted(jobTypes, key=lambda tag: tag.name, reverse=options.
            sortReverse)
    elif options.sortCategory == 'count':
        return sorted(jobTypes, key=lambda tag: tag.total_number, reverse=
            options.sortReverse)