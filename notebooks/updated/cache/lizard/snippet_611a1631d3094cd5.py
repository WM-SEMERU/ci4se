def _compute_heating_rates(self):
    self.LW_to_atm = self._compute_emission()
    self.SW_to_atm = self._compute_reflected_flux()
    self.heating_rate['Ts'
        ] = self.LW_from_atm - self.LW_to_atm + self.SW_from_atm - self.SW_to_atm