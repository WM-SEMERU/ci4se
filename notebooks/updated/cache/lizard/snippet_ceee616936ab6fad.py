def getContactItems(self, person):
    return person.store.query(PhoneNumber, PhoneNumber.person == person)