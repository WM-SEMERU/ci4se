def max_voltage_step(self):
    steps = [(self.voltage_pairs[i].voltage - self.voltage_pairs[i + 1].
        voltage) for i in range(len(self.voltage_pairs) - 1)]
    return max(steps) if len(steps) > 0 else 0