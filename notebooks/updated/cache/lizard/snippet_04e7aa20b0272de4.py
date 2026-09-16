def findfile(self, old, new):
    if exists(old):
        return old
    elif exists(new):
        return new
    else:
        debug('broken patch from Google Code, stripping prefixes..')
        if old.startswith(b'a/') and new.startswith(b'b/'):
            old, new = old[2:], new[2:]
            debug('   %s' % old)
            debug('   %s' % new)
            if exists(old):
                return old
            elif exists(new):
                return new
        return None