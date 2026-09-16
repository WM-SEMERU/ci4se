def load_saved_records(self, status, records):
    if isinstance(status, ALDBStatus):
        self._status = status
    else:
        self._status = ALDBStatus(status)
    for mem_addr in records:
        rec = records[mem_addr]
        control_flags = int(rec.get('control_flags', 0))
        group = int(rec.get('group', 0))
        rec_addr = rec.get('address', '000000')
        data1 = int(rec.get('data1', 0))
        data2 = int(rec.get('data2', 0))
        data3 = int(rec.get('data3', 0))
        self[int(mem_addr)] = ALDBRecord(int(mem_addr), control_flags,
            group, rec_addr, data1, data2, data3)
    if self._status == ALDBStatus.LOADED:
        keys = list(self._records.keys())
        keys.sort(reverse=True)
        first_key = keys[0]
        self._mem_addr = first_key