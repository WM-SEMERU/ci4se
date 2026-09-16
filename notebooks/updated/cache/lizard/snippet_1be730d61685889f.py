def growth_volatility(eqdata, **kwargs):
    _window = kwargs.get('window', 20)
    _selection = kwargs.get('selection', 'Adj Close')
    _outputcol = kwargs.get('outputcol', 'Growth Risk')
    _growthdata = simple.growth(eqdata, selection=_selection)
    return volatility(_growthdata, outputcol=_outputcol, window=_window)