def make_password(password, salt=None, hasher='default'):
    if password is None:
        return UNUSABLE_PASSWORD_PREFIX + get_random_string(
            UNUSABLE_PASSWORD_SUFFIX_LENGTH)
    hasher = bCryptPasswordHasher
    if not salt:
        salt = hasher.salt()
    return hasher.encode(password, salt)