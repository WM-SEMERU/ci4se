def analyze_overs(self1):
    self1.dif1 = [(self1.overs[i][0] - self1.overs[i - 1][0]) for i in
        range(1, len(self1.overs))]
    self1.dif2 = [(self1.overs[i][1] - self1.overs[i - 1][1]) for i in
        range(1, len(self1.overs))]
    self1.start1 = self1.overs[0][0] == 0
    self1.start2 = self1.overs[0][1] == 0
    self1.end1 = self1.overs[-1][0] == len(self1.tx_obj1.exons) - 1
    self1.end2 = self1.overs[-1][1] == len(self1.tx_obj2.exons) - 1
    return