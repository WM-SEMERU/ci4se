def getAttrib(self, attribId):
    Observable.setChanged(self)
    Observable.notifyObservers(self, CardConnectionEvent('attrib', [attribId]))
    data = self.doGetAttrib(attribId)
    if self.errorcheckingchain is not None:
        self.errorcheckingchain[0](data)
    return data