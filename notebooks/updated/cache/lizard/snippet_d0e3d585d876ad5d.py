def dataframe(self):
    if self._dataframe is None:
        try:
            import pandas as pd
        except ImportError:
            raise RuntimeError(
                "To enable dataframe support, run 'pip install datadotworld[pandas]'"
                )
        self._dataframe = pd.DataFrame.from_records(self._iter_rows(),
            coerce_float=True)
    return self._dataframe