def __dp(self):
    dp = self.__client.options.port
    if dp is None:
        return None
    else:
        return self.__find(dp)