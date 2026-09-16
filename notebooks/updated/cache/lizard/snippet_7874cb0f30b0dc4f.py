def wrap_results_for_axis(self):
    results = self.results
    result = self.obj._constructor(data=results)
    if not isinstance(results[0], ABCSeries):
        try:
            result.index = self.res_columns
        except ValueError:
            pass
    try:
        result.columns = self.res_index
    except ValueError:
        pass
    return result