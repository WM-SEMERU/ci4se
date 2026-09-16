def ReadClientStartupInfoHistory(self, client_id, timerange=None):
    from_time, to_time = self._ParseTimeRange(timerange)
    history = self.startup_history.get(client_id)
    if not history:
        return []
    res = []
    for ts in sorted(history, reverse=True):
        if ts < from_time or ts > to_time:
            continue
        client_data = rdf_client.StartupInfo.FromSerializedString(history[ts])
        client_data.timestamp = ts
        res.append(client_data)
    return res