def storage_pools(self):
    if not self.__storage_pools:
        self.__storage_pools = StoragePools(self.__connection)
    return self.__storage_pools