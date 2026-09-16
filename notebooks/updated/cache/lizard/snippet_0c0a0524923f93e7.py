def create_database_info(self, name, vendor, channel):
    return DbInfoHandle(self._nsdk, self._nsdk.databaseinfo_create(name,
        vendor, channel.type_, channel.endpoint))