def association(self, group_xid):
    association = {'groupXid': group_xid}
    self._indicator_data.setdefault('associatedGroups', []).append(association)