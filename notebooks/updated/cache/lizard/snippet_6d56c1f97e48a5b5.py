def init(self):
    if not self.export_enable:
        return None
    try:
        db = InfluxDBClient(host=self.host, port=self.port, username=self.
            user, password=self.password, database=self.db)
        get_all_db = [i['name'] for i in db.get_list_database()]
    except InfluxDBClientError as e:
        logger.critical("Cannot connect to InfluxDB database '%s' (%s)" % (
            self.db, e))
        sys.exit(2)
    if self.db in get_all_db:
        logger.info('Stats will be exported to InfluxDB server: {}'.format(
            db._baseurl))
    else:
        logger.critical(
            "InfluxDB database '%s' did not exist. Please create it" % self.db)
        sys.exit(2)
    return db