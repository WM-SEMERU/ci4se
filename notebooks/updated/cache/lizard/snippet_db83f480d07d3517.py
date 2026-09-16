def get_flow_by_idx(self, idx, bus):
    P, Q = [], []
    if type(idx) is not list:
        idx = [idx]
    if type(bus) is not list:
        bus = [bus]
    for line_idx, bus_idx in zip(idx, bus):
        line_int = self.uid[line_idx]
        if bus_idx == self.bus1[line_int]:
            P.append(self.P1[line_int])
            Q.append(self.Q1[line_int])
        elif bus_idx == self.bus2[line_int]:
            P.append(self.P2[line_int])
            Q.append(self.Q2[line_int])
    return matrix(P), matrix(Q)