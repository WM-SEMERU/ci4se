def add_contact_person(self, person):
    if not isinstance(person, ContactPersonDesc):
        raise TypeError('person must be of type ContactPersonDesc')
    self._contact_person.append(person)