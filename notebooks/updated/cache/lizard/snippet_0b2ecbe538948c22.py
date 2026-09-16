def get_historical_klines(symbol, interval, start_str, end_str=None):
    client = Client('', '')
    output_data = []
    limit = 500
    timeframe = interval_to_milliseconds(interval)
    start_ts = date_to_milliseconds(start_str)
    end_ts = None
    if end_str:
        end_ts = date_to_milliseconds(end_str)
    idx = 0
    symbol_existed = False
    while True:
        temp_data = client.get_klines(symbol=symbol, interval=interval,
            limit=limit, startTime=start_ts, endTime=end_ts)
        if not symbol_existed and len(temp_data):
            symbol_existed = True
        if symbol_existed:
            output_data += temp_data
            start_ts = temp_data[len(temp_data) - 1][0] + timeframe
        else:
            start_ts += timeframe
        idx += 1
        if len(temp_data) < limit:
            break
        if idx % 3 == 0:
            time.sleep(1)
    return output_data