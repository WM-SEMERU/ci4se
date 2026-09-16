def validate_setup(transactions):
    if not transactions:
        return True
    try:
        first, second = transactions[:2]
    except ValueError:
        print(
            'Error: vacationrc file must have both initial days and rates entries'
            )
        return False
    parts1, parts2 = first.split(), second.split()
    if parts1[0] != parts2[0]:
        print('Error: First two entries in vacationrc must have the same date')
        return False
    if 'rate' not in (parts1[1], parts2[1]) or 'days' not in (parts1[1],
        parts2[1]):
        print('Error: First two entries in vacationrc must set days and rate')
        return False
    return True