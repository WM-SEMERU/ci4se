def write_dataframe_to_idb(self, ticker):
    cachepath = self._cache
    cachefile = '%s/%s-1M.csv.gz' % (cachepath, ticker)
    if not os.path.exists(cachefile):
        log.warn('Import file does not exist: %s' % cachefile)
        return
    df = pd.read_csv(cachefile, compression='infer', header=0,
        infer_datetime_format=True)
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df.set_index('Datetime')
    df = df.drop(['Date', 'Time'], axis=1)
    try:
        self.dfdb.write_points(df, ticker)
    except InfluxDBClientError as err:
        log.error('Write to database failed: %s' % err)