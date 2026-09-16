def set_result(self, values, visible_columns={}):
    exitcode = values.pop('exitcode', None)
    if exitcode is not None:
        self.values['@exitcode'] = exitcode
        exitcode = util.ProcessExitCode.from_raw(exitcode)
        if exitcode.signal:
            self.values['@exitsignal'] = exitcode.signal
        else:
            self.values['@returnvalue'] = exitcode.value
    for key, value in values.items():
        if key == 'walltime':
            self.walltime = value
        elif key == 'cputime':
            self.cputime = value
        elif key == 'memory':
            self.values['memUsage'] = value
        elif key == 'cpuenergy' and not isinstance(value, (str, bytes)):
            energy = intel_cpu_energy.format_energy_results(value)
            for energy_key, energy_value in energy.items():
                if energy_key != 'cpuenergy':
                    energy_key = '@' + energy_key
                self.values[energy_key] = energy_value
        elif key == 'cpuenergy':
            self.values[key] = value
        elif key in visible_columns:
            self.values[key] = value
        else:
            self.values['@' + key] = value
    self.after_execution(exitcode, termination_reason=values.get(
        'terminationreason'))