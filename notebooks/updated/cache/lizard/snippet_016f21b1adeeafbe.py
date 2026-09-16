def add_recording_behavior(self, component, runnable):
    simulation = component.simulation
    for rec in simulation.records:
        rec.id = runnable.id
        self.current_record_target.add_variable_recorder(self.
            current_data_output, rec)