def add_datetime(dataframe, timestamp_key='UNIXTIME'):

    def convert_data(timestamp):
        return datetime.fromtimestamp(float(timestamp) / 1000.0, UTC_TZ)
    try:
        log.debug('Adding DATETIME column to the data')
        converted = dataframe[timestamp_key].apply(convert_data)
        dataframe['DATETIME'] = converted
    except KeyError:
        log.warning('Could not add DATETIME column')