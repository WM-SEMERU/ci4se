def cleanup(self):
    allList = []
    allList.extend(self.cur.execute('SELECT keywordid FROM keyword;'))
    usedList = []
    usedList.extend(self.cur.execute('SELECT keywordid FROM notekeyword;'))
    unusedList = [val for val in allList if val not in usedList]
    for key in unusedList:
        if self.debug:
            print('About to delete keyword with ID %s' % key)
        try:
            self.cur.execute('DELETE FROM keyword WHERE keywordId = ?;', key)
        except:
            self.error('There was a problem deleting keyword %s' % key)
    self.con.commit()