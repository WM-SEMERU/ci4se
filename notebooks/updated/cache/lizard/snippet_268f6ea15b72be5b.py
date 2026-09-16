def launch_simulation(self, parameter):
    return next(SimulationRunner.run_simulations(self, [parameter], self.
        data_folder))