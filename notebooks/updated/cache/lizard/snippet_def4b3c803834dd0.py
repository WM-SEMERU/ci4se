def _get_licences():
    licenses = _LICENSES
    for license in licenses:
        print('{license_name} [{license_code}]'.format(license_name=
            licenses[license], license_code=license))