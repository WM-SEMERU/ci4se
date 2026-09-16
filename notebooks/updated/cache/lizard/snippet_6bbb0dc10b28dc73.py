def set_tick(self, index, interval):
    name = self.tick_name(index)
    if name is None:
        return pack_error(ControllerSubsystem.SENSOR_GRAPH, Error.
            INVALID_ARRAY_KEY)
    self.ticks[name] = interval
    return Error.NO_ERROR