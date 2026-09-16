def get_ansible_by_id(self, ansible_id):
    for elem in self.ansible_hosts:
        if elem.id == ansible_id:
            return elem
    return None