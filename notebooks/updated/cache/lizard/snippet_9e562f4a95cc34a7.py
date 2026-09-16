def VerifyRow(self, parser_mediator, row):
    try:
        time_elements_tuple = self._GetTimeElementsTuple(row['time'])
    except (TypeError, ValueError):
        return False
    try:
        dfdatetime_time_elements.TimeElements(time_elements_tuple=
            time_elements_tuple)
    except ValueError:
        return False
    try:
        my_event = int(row['event'], 10)
    except (TypeError, ValueError):
        return False
    if my_event < 1 or my_event > 77:
        return False
    try:
        category = int(row['cat'], 10)
    except (TypeError, ValueError):
        return False
    if category < 1 or category > 4:
        return False
    return True