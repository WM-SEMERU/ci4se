def delete_contact(self, contact_id):
    url = self.CONTACTS_ID_URL % contact_id
    connection = Connection(self.token)
    connection.set_url(self.production, url)
    return connection.delete_request()