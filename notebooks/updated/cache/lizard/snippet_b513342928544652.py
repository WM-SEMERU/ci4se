def is_address_commited(self, address):
    try:
        mbi = self.mquery(address)
    except WindowsError:
        e = sys.exc_info()[1]
        if e.winerror == win32.ERROR_INVALID_PARAMETER:
            return False
        raise
    return mbi.is_commited()