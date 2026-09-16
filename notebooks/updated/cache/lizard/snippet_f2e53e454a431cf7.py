def getContactItems(self, person):
    return person.store.query(EmailAddress, EmailAddress.person == person)