def base64_b64encode(instr):
    return salt.utils.stringutils.to_unicode(base64.b64encode(salt.utils.
        stringutils.to_bytes(instr)), encoding='utf8' if salt.utils.
        platform.is_windows() else None)