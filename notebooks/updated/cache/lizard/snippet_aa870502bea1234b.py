def __placeSellShortOrder(self, tick):
    share = math.floor(self.__strategy.getAccountCopy().getCash() / float(
        tick.close))
    sellShortOrder = Order(accountId=self.__strategy.accountId, action=
        Action.SELL_SHORT, is_market=True, security=self.__security, share=
        share)
    if self.__strategy.placeOrder(sellShortOrder):
        self.__buyOrder = sellShortOrder
        stopOrder = Order(accountId=self.__strategy.accountId, action=
            Action.BUY_TO_COVER, is_stop=True, security=self.__security,
            price=tick.close * 1.05, share=0 - share)
        self.__placeStopOrder(stopOrder)