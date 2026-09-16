def get_acs(self):
    import predix.security.acs
    acs = predix.security.acs.AccessControl()
    return acs