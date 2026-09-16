def MatchQuality(cls, record_data, record_count=1):
    if record_count > 1:
        return MatchQuality.NoMatch
    cmd, _address, _resp_length, _payload = cls._parse_rpc_info(record_data)
    if cmd == PersistGraphRecord.RPC_ID:
        return MatchQuality.PerfectMatch
    return MatchQuality.NoMatch