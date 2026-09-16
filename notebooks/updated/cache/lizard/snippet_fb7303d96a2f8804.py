def orderExecuted(self, orderDict):
    for orderId, order in orderDict.items():
        if order.symbol in self.__trakers.keys():
            self.__trakers[order.symbol].orderExecuted(orderId)