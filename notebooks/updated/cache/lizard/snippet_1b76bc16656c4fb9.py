def get_fba_obj_flux(self, objective):
    flux_result = self.solve_fba(objective)
    return flux_result.get_value(self._v_wt[objective])