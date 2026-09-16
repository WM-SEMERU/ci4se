def pull(self, bookName=None, sheetName=None):
    if bookName is None and self.bookName:
        bookName = self.bookName
    if sheetName is None and self.sheetName:
        sheetName = self.sheetName
    if bookName is None:
        bookName = OR.activeBook()
    if bookName and sheetName is None:
        sheetName = OR.activeSheet()
    if not bookName or not sheetName:
        print("can't figure out where to pull from! [%s]%s" % (bookName,
            sheetName))
        return
    poSheet = OR.getSheet(bookName, sheetName)
    self.bookName = bookName
    self.sheetName = sheetName
    self.desc = poSheet.GetLongName()
    self.colNames = [poCol.GetName() for poCol in poSheet.Columns()]
    self.colDesc = [poCol.GetLongName() for poCol in poSheet.Columns()]
    self.colUnits = [poCol.GetUnits() for poCol in poSheet.Columns()]
    self.colComments = [poCol.GetComments() for poCol in poSheet.Columns()]
    self.colTypes = [poCol.GetType() for poCol in poSheet.Columns()]
    self.colData = [poCol.GetData() for poCol in poSheet.Columns()]