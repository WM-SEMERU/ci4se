def import_powerflow_results(self, session):
    pypsa_io.import_pfa_bus_results(session, self)
    pypsa_io.import_pfa_line_results(session, self)