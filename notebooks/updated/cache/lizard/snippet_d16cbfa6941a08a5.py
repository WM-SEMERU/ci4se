def get_channel_names(self):
    names_s, names_n = self.channel_names_s, self.channel_names_n
    if self._channel_naming == '$PnS':
        channel_names, channel_names_alternate = names_s, names_n
    else:
        channel_names, channel_names_alternate = names_n, names_s
    if len(channel_names) == 0:
        channel_names = channel_names_alternate
    if len(set(channel_names)) != len(channel_names):
        msg = (
            'The default channel names (defined by the {} parameter in the FCS file) were not unique. To avoid problems in downstream analysis, the channel names have been switched to the alternate channel names defined in the FCS file. To avoid seeing this warning message, explicitly instruct the FCS parser to use the alternate channel names by specifying the channel_naming parameter.'
            )
        msg = msg.format(self._channel_naming)
        warnings.warn(msg)
        channel_names = channel_names_alternate
    return channel_names