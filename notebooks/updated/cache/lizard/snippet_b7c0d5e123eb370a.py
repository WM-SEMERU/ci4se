def terminateMember(self, clusterId, memberId):
    self.send_terminateMember(clusterId, memberId)
    return self.recv_terminateMember()