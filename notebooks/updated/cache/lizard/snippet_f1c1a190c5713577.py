def get_profile_name(org_vm, profile_inst):
    try:
        org = org_vm.tovalues(profile_inst['RegisteredOrganization'])
        name = profile_inst['RegisteredName']
        vers = profile_inst['RegisteredVersion']
        return org, name, vers
    except TypeError as te:
        print('ORG_VM.TOVALUES FAILED. inst=%s, Exception %s' % (
            profile_inst, te))
    except ValueError as ve:
        print('ORG_VM.TOVALUES FAILED. inst=%s, Exception %s' % (
            profile_inst, ve))
    return 'ERR', 'ERR', 'ERR'