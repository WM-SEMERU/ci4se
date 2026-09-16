def curtailment(self):
    if self._curtailment is not None:
        return self._curtailment
    elif isinstance(self.grid.network.timeseries._curtailment, pd.DataFrame):
        if isinstance(self.grid.network.timeseries.curtailment.columns, pd.
            MultiIndex):
            if self.weather_cell_id:
                try:
                    return self.grid.network.timeseries.curtailment[self.
                        type, self.weather_cell_id]
                except KeyError:
                    logger.exception(
                        'No curtailment time series for type {} and weather cell ID {} given.'
                        .format(self.type, self.weather_cell_id))
                    raise
            else:
                logger.exception(
                    'No weather cell ID provided for fluctuating generator {}.'
                    .format(repr(self)))
                raise KeyError
        else:
            try:
                return self.grid.network.timeseries.curtailment[self.type]
            except KeyError:
                logger.exception(
                    'No curtailment time series for type {} given.'.format(
                    self.type))
                raise
    else:
        return None