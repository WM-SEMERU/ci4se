def do_diagnostics(self):
    self.OLR = self.subprocess['LW'].flux_to_space
    self.LW_down_sfc = self.subprocess['LW'].flux_to_sfc
    self.LW_up_sfc = self.subprocess['LW'].flux_from_sfc
    self.LW_absorbed_sfc = self.LW_down_sfc - self.LW_up_sfc
    self.LW_absorbed_atm = self.subprocess['LW'].absorbed
    self.LW_emission = self.subprocess['LW'].emission
    self.ASR = self.subprocess['SW'].flux_from_space - self.subprocess['SW'
        ].flux_to_space
    self.SW_absorbed_atm = self.subprocess['SW'].absorbed
    self.SW_down_sfc = self.subprocess['SW'].flux_to_sfc
    self.SW_up_sfc = self.subprocess['SW'].flux_from_sfc
    self.SW_absorbed_sfc = self.SW_down_sfc - self.SW_up_sfc
    self.SW_up_TOA = self.subprocess['SW'].flux_to_space
    self.SW_down_TOA = self.subprocess['SW'].flux_from_space
    self.planetary_albedo = self.subprocess['SW'
        ].flux_to_space / self.subprocess['SW'].flux_from_space