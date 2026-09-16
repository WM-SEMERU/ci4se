def get_providing_power_source_type(self):
    power_status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(pointer(power_status)):
        raise WinError()
    return POWER_TYPE_MAP[power_status.ACLineStatus]