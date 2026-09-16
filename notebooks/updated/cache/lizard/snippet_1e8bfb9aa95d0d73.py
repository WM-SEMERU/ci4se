def cancel_guests(self, host_id):
    result = []
    guests = self.host.getGuests(id=host_id, mask='id,fullyQualifiedDomainName'
        )
    if guests:
        for vs in guests:
            status_info = {'id': vs['id'], 'fqdn': vs[
                'fullyQualifiedDomainName'], 'status': self._delete_guest(
                vs['id'])}
            result.append(status_info)
    return result