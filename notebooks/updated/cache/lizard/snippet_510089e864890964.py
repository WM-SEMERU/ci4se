def pa11y_counts(results):
    num_error = 0
    num_warning = 0
    num_notice = 0
    for result in results:
        if result['type'] == 'error':
            num_error += 1
        elif result['type'] == 'warning':
            num_warning += 1
        elif result['type'] == 'notice':
            num_notice += 1
    return num_error, num_warning, num_notice