def _json_to_registrations(data, section):
    registrations = []
    person_threads = {}
    for reg_data in data.get('Registrations', []):
        registration = Registration()
        registration.section = section
        registration.is_active = reg_data['IsActive']
        registration.is_credit = reg_data['IsCredit']
        registration.is_auditor = reg_data['Auditor']
        registration.is_independent_start = reg_data['IsIndependentStart']
        if len(reg_data['StartDate']):
            registration.start_date = parse(reg_data['StartDate'])
        if len(reg_data['EndDate']):
            registration.end_date = parse(reg_data['EndDate'])
        if len(reg_data['RequestDate']):
            registration.request_date = parse(reg_data['RequestDate'])
        registration.request_status = reg_data['RequestStatus']
        registration.duplicate_code = reg_data['DuplicateCode']
        registration.credits = reg_data['Credits']
        registration.repository_timestamp = datetime.strptime(reg_data[
            'RepositoryTimeStamp'], '%m/%d/%Y %H:%M:%S %p')
        registration.repeat_course = reg_data['RepeatCourse']
        registration.grade = reg_data['Grade']
        registration._uwregid = reg_data['Person']['RegID']
        if registration._uwregid not in person_threads:
            thread = SWSPersonByRegIDThread()
            thread.regid = registration._uwregid
            thread.start()
            person_threads[registration._uwregid] = thread
        registrations.append(registration)
    for registration in registrations:
        thread = person_threads[registration._uwregid]
        thread.join()
        registration.person = thread.person
        del registration._uwregid
    return registrations