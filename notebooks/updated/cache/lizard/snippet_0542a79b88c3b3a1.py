def inDignities(self, idA, idB):
    objA = self.chart.get(idA)
    info = essential.getInfo(objA.sign, objA.signlon)
    return [dign for dign, ID in info.items() if ID == idB]