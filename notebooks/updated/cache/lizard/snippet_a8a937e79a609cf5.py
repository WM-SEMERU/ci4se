def intSize(self, obj):
    if obj < 0:
        return 8
    elif obj <= 255:
        return 1
    elif obj <= 65535:
        return 2
    elif obj <= 4294967295:
        return 4
    elif obj <= 9223372036854775807:
        return 8
    elif obj <= 18446744073709551615:
        return 16
    else:
        raise InvalidPlistException(
            "Core Foundation can't handle integers with size greater than 8 bytes."
            )