def updateDataset(self):
    self.__updateDataItem()
    self.__countNbRecords()
    self.__columns = self.__parseColumns()