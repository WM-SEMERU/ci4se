def execute_on_member(self, member, task):
    uuid = self._get_uuid()
    address = member.address
    return self._execute_on_member(address, uuid, self._to_data(task))