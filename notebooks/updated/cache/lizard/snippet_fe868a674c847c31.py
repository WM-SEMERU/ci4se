def subject(self, value):
    if isinstance(value, Subject):
        if value.personalization is not None:
            try:
                personalization = self._personalizations[value.personalization]
                has_internal_personalization = True
            except IndexError:
                personalization = Personalization()
                has_internal_personalization = False
            personalization.subject = value.subject
            if not has_internal_personalization:
                self.add_personalization(personalization, index=value.
                    personalization)
        else:
            self._subject = value
    else:
        self._subject = Subject(value)