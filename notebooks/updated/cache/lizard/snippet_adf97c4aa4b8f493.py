def is_valid_uuid(uuid):
    try:
        if len(uuid) == 4:
            if int(uuid, 16) < 0:
                return False
        elif len(uuid) == 8:
            if int(uuid, 16) < 0:
                return False
        elif len(uuid) == 36:
            pieces = uuid.split('-')
            if len(pieces) != 5 or len(pieces[0]) != 8 or len(pieces[1]
                ) != 4 or len(pieces[2]) != 4 or len(pieces[3]) != 4 or len(
                pieces[4]) != 12:
                return False
            [int(p, 16) for p in pieces]
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False
    return True