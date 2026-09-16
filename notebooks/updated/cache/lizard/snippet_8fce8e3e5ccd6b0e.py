def set_user_password(uid, mode='set_password', password=None, **kwargs):
    with _IpmiCommand(**kwargs) as s:
        s.set_user_password(uid, mode='set_password', password=password)
    return True