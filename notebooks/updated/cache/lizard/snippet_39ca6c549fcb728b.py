def get_json_shift(year, month, day, unit, count, period, symbol):
    epochs = date.get_end_start_epochs(year, month, day, 'last', unit, count)
    return chart_json(epochs['shifted'], epochs['initial'], period, symbol)[0]