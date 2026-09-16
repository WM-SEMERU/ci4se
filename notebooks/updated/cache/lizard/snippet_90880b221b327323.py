def wait(self, wait_time=0):
    if self.__result:
        return True
    data = self.rdb.brpop(self.urn, wait_time)
    if data:
        self.rdb.delete(self.urn)
        data = json.loads(data[1])
        self.__result = data
        return True
    else:
        return False