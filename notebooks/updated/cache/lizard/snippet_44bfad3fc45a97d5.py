def GetEventData(self, data_type):
    event_data = events.EventData(data_type=data_type)
    for property_name, property_value in iter(self._properties.items()):
        if isinstance(property_value, py2to3.BYTES_TYPE):
            property_value = repr(property_value)
        setattr(event_data, property_name, property_value)
    return event_data