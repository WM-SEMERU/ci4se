def get_providing_power_source_type(self):
    type = self.power_source_type()
    if type == common.POWER_TYPE_AC:
        if self.is_ac_online():
            return common.POWER_TYPE_AC
        elif type == common.POWER_TYPE_BATTERY:
            if self.is_battery_present() and self.is_battery_discharging():
                return common.POWER_TYPE_BATTERY
            else:
                warnings.warn('UPS is not supported.')
    return common.POWER_TYPE_AC