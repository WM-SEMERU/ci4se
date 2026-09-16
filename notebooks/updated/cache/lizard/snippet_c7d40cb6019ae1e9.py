def rand_alphastr(length, lower=True, upper=True):
    if lower is True and upper is True:
        return rand_str(length, allowed=string.ascii_letters)
    if lower is True and upper is False:
        return rand_str(length, allowed=string.ascii_lowercase)
    if lower is False and upper is True:
        return rand_str(length, allowed=string.ascii_uppercase)
    else:
        raise Exception