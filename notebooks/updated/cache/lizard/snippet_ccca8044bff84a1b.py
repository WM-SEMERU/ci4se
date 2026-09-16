def appropriate_for(self, usage, alg='HS256'):
    try:
        _use = USE[usage]
    except:
        raise ValueError('Unknown key usage')
    else:
        if not self.use or self.use == _use:
            if _use == 'sig':
                return self.get_key()
            else:
                return self.encryption_key(alg)
        raise WrongUsage("This key can't be used for {}".format(usage))