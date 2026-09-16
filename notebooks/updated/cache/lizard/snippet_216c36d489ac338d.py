def removereadergroup(self, group):
    hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
    if 0 != hresult:
        raise error('Failed to establish context: ' + SCardGetErrorMessage(
            hresult))
    try:
        hresult = SCardForgetReaderGroup(hcontext, group)
        if hresult != 0:
            raise error('Unable to forget reader group: ' +
                SCardGetErrorMessage(hresult))
        else:
            innerreadergroups.removereadergroup(self, group)
    finally:
        hresult = SCardReleaseContext(hcontext)
        if 0 != hresult:
            raise error('Failed to release context: ' +
                SCardGetErrorMessage(hresult))