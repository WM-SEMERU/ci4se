def get_channel_property_names(self, channel_id=None):
    if channel_id is None:
        property_names = []
        for channel_id in self.get_channel_ids():
            curr_property_names = self.get_channel_property_names(channel_id
                =channel_id)
            for curr_property_name in curr_property_names:
                property_names.append(curr_property_name)
        property_names = sorted(list(set(property_names)))
        return property_names
    if isinstance(channel_id, (int, np.integer)):
        if channel_id in self.get_channel_ids():
            if channel_id not in self._channel_properties:
                self._channel_properties[channel_id] = {}
            property_names = sorted(self._channel_properties[channel_id].keys()
                )
            return property_names
        else:
            raise ValueError(str(channel_id) + ' is not a valid channel_id')
    else:
        raise ValueError(str(channel_id) + ' must be an int')