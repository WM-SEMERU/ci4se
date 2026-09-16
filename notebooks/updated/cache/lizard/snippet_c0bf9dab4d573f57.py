def verify(self, store, flags, data=None, certs=None):
    bio = None
    if data != None:
        bio_obj = Membio(data)
        bio = bio_obj.bio
    if certs is not None and len(certs) > 0:
        certstack_obj = StackOfX509(certs)
        certstack = certstack_obj.ptr
    else:
        certstack = None
    res = libcrypto.CMS_verify(self.ptr, certstack, store.store, bio, None,
        flags)
    return res > 0