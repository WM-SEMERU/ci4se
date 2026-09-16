def scrubID(ID):
    try:
        if type(ID) == list:
            return int(ID[0])
        elif type(ID) == str:
            return int(ID)
        elif type(ID) == int:
            return ID
        elif type(ID) == unicode:
            return int(ID)
    except ValueError:
        return None