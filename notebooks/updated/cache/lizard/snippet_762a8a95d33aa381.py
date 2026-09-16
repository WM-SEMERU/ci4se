def assert_is_instance(obj, cls, msg_fmt='{msg}'):
    if not isinstance(obj, cls):
        msg = '{!r} is an instance of {!r}, expected {!r}'.format(obj, obj.
            __class__, cls)
        types = cls if isinstance(cls, tuple) else (cls,)
        fail(msg_fmt.format(msg=msg, obj=obj, types=types))