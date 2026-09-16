def get_last_activity(session):
    try:
        return datetime.strptime(session['_session_security'],
            '%Y-%m-%dT%H:%M:%S.%f')
    except AttributeError:
        return datetime.now()
    except TypeError:
        return datetime.now()