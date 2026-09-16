def elcm_profile_delete(irmc_info, profile_name):
    resp = elcm_request(irmc_info, method='DELETE', path=
        URL_PATH_PROFILE_MGMT + profile_name)
    if resp.status_code == 200:
        return
    elif resp.status_code == 404:
        raise ELCMProfileNotFound(
            'Profile "%s" not found in the profile store.' % profile_name)
    else:
        raise scci.SCCIClientError(
            'Failed to delete profile "%(profile)s" with error code %(error)s'
             % {'profile': profile_name, 'error': resp.status_code})