def get_security_attributes_for_user(user=None):
    if user is None:
        user = get_current_user()
    assert isinstance(user, security.TOKEN_USER
        ), 'user must be TOKEN_USER instance'
    SD = security.SECURITY_DESCRIPTOR()
    SA = security.SECURITY_ATTRIBUTES()
    SA.descriptor = SD
    SA.bInheritHandle = 1
    ctypes.windll.advapi32.InitializeSecurityDescriptor(ctypes.byref(SD),
        security.SECURITY_DESCRIPTOR.REVISION)
    ctypes.windll.advapi32.SetSecurityDescriptorOwner(ctypes.byref(SD),
        user.SID, 0)
    return SA