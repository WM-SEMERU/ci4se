def check_multi_dimensional_coords(self, ds):
    ret_val = []
    for coord in self._find_aux_coord_vars(ds):
        variable = ds.variables[coord]
        if variable.ndim < 2:
            continue
        not_matching = TestCtx(BaseCheck.MEDIUM, self.section_titles['5'])
        not_matching.assert_true(coord not in variable.dimensions,
            '{} shares the same name as one of its dimensions'.format(coord))
        ret_val.append(not_matching.to_result())
    return ret_val