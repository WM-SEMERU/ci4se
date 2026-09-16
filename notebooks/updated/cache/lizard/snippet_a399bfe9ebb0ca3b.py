def get_time_remaining_estimate(self):
    all_energy_now = []
    all_power_now = []
    try:
        type = self.power_source_type()
        if type == common.POWER_TYPE_AC:
            if self.is_ac_online(supply_path):
                return common.TIME_REMAINING_UNLIMITED
        elif type == common.POWER_TYPE_BATTERY:
            if self.is_battery_present() and self.is_battery_discharging():
                energy_full, energy_now, power_now = self.get_battery_state()
                all_energy_now.append(energy_now)
                all_power_now.append(power_now)
        else:
            warnings.warn('UPS is not supported.')
    except (RuntimeError, IOError) as e:
        warnings.warn('Unable to read system power information!', category=
            RuntimeWarning)
    if len(all_energy_now) > 0:
        try:
            return sum([(energy_now / power_now * 60.0) for energy_now,
                power_now in zip(all_energy_now, all_power_now)])
        except ZeroDivisionError as e:
            warnings.warn('Unable to calculate time remaining estimate: {0}'
                .format(e), category=RuntimeWarning)
            return common.TIME_REMAINING_UNKNOWN
    else:
        return common.TIME_REMAINING_UNKNOWN