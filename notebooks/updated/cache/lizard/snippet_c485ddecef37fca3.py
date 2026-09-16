def cancelHistoricalData(self, bars: BarDataList):
    self.client.cancelHistoricalData(bars.reqId)
    self.wrapper.endSubscription(bars)