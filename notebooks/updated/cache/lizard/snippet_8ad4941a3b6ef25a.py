def delete_contacts(self, ids: List[int]):
    contacts = []
    for i in ids:
        try:
            input_user = self.resolve_peer(i)
        except PeerIdInvalid:
            continue
        else:
            if isinstance(input_user, types.InputPeerUser):
                contacts.append(input_user)
    return self.send(functions.contacts.DeleteContacts(id=contacts))