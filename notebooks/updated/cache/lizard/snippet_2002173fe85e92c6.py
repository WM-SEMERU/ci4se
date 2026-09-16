def sign_in(user, user_type=None, date=None, time_in=None):
    now = datetime.today()
    if date is None:
        date = now.date()
    if time_in is None:
        time_in = now.time()
    if user_type is None:
        if user.is_student and user.is_tutor:
            raise AmbiguousUserType('User is both a student and a tutor.')
        elif user.is_student:
            user_type = 'student'
        elif user.is_tutor:
            user_type = 'tutor'
        else:
            raise ValueError('Unknown user type.')
    new_entry = Entry(uuid=str(uuid.uuid4()), date=date, time_in=time_in,
        time_out=None, user_id=user.user_id, user_type=user_type, user=user)
    logger.info('{} ({}) signed in.'.format(new_entry.user_id, new_entry.
        user_type))
    return new_entry