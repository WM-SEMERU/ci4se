def srp1(*args, **kargs):
    ans, _ = srp(*args, **kargs)
    if len(ans) > 0:
        return ans[0][1]
    else:
        return None