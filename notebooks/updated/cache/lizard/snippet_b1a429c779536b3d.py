def battery_status_send(self, id, battery_function, type, temperature,
    voltages, current_battery, current_consumed, energy_consumed,
    battery_remaining, force_mavlink1=False):
    return self.send(self.battery_status_encode(id, battery_function, type,
        temperature, voltages, current_battery, current_consumed,
        energy_consumed, battery_remaining), force_mavlink1=force_mavlink1)