def check_offline_configuration(self):
    quit_on_start = False
    database_url = self.config.get('Database Parameters', 'database_url')
    host = self.config.get('Server Parameters', 'host', 'localhost')
    if database_url[:6] != 'sqlite':
        print(
            "*** Error: config.txt option 'database_url' set to use mysql://.  Please change this sqllite:// while in cabin mode."
            )
        quit_on_start = True
    if host != 'localhost':
        print(
            "*** Error: config option 'host' is not set to localhost. Please change this to localhost while in cabin mode."
            )
        quit_on_start = True
    if quit_on_start:
        exit()