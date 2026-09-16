def decodeRPCErrorMsg(e):
    found = re.search(
        """(10 assert_exception: Assert Exception
|3030000 tx_missing_posting_auth).*: (.*)
"""
        , str(e), flags=re.M)
    if found:
        return found.group(2).strip()
    else:
        return str(e)