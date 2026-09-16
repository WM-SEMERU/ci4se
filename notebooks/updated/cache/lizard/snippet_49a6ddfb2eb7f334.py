def getConfig(self, type='online', format='elegant'):
    return list(list(self.dumpConfigDict[type](format).values())[0].values())[0
        ]