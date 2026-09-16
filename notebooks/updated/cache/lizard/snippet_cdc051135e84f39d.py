def __parse_affiliations_json(self, affiliations, uuid):
    enrollments = []
    for affiliation in affiliations.values():
        name = self.__encode(affiliation['name'])
        try:
            start_date = str_to_datetime(affiliation['active'])
            end_date = str_to_datetime(affiliation['inactive'])
        except InvalidDateError as e:
            raise InvalidFormatError(cause=str(e))
        if not start_date and not end_date:
            continue
        if not start_date:
            start_date = MIN_PERIOD_DATE
        if not end_date:
            end_date = MAX_PERIOD_DATE
        org = self._organizations.get(name, None)
        if org:
            start_date = org.active if start_date < org.active else start_date
            end_date = org.inactive if end_date > org.inactive else end_date
        if not org:
            org = Organization(name=name)
            org.active = MIN_PERIOD_DATE
            org.inactive = MAX_PERIOD_DATE
        enrollment = Enrollment(start=start_date, end=end_date,
            organization=org)
        enrollments.append(enrollment)
    return enrollments