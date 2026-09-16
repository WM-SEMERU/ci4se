def progress_bar(items_total, items_progress, columns=40, base_char='.',
    progress_char='#', percentage=False, prefix='', postfix=''):
    bins_total = int(float(items_total) / columns) + 1
    bins_progress = int(float(items_progress) / float(items_total) * bins_total
        ) + 1
    progress = prefix
    progress += progress_char * bins_progress
    progress += base_char * (bins_total - bins_progress)
    if percentage:
        progress_percentage = float(items_progress) / float(items_total) * 100
        postfix = ' ' + str(round(progress_percentage, 2)) + '% ' + postfix
    progress += postfix
    return progress