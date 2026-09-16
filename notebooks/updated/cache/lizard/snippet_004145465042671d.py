def found_duplicates(counts):
    _logger.warning('Duplicated markers found')
    for marker, count in counts:
        _logger.warning(' - {}: {:,d} times'.format(marker, count))
    _logger.warning(
        "Appending ':dupX' to the duplicated markers according to their location in the file."
        )