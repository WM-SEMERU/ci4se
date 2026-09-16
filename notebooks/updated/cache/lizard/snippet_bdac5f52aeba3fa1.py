def _DetermineOperatingSystem(self, searcher):
    find_specs = [file_system_searcher.FindSpec(location='/etc',
        case_sensitive=False), file_system_searcher.FindSpec(location=
        '/System/Library', case_sensitive=False), file_system_searcher.
        FindSpec(location='/Windows/System32', case_sensitive=False),
        file_system_searcher.FindSpec(location='/WINNT/System32',
        case_sensitive=False), file_system_searcher.FindSpec(location=
        '/WINNT35/System32', case_sensitive=False), file_system_searcher.
        FindSpec(location='/WTSRV/System32', case_sensitive=False)]
    locations = []
    for path_spec in searcher.Find(find_specs=find_specs):
        relative_path = searcher.GetRelativePath(path_spec)
        if relative_path:
            locations.append(relative_path.lower())
    windows_locations = set(['/windows/system32', '\\windows\\system32',
        '/winnt/system32', '\\winnt\\system32', '/winnt35/system32',
        '\\winnt35\\system32', '\\wtsrv\\system32', '/wtsrv/system32'])
    operating_system = definitions.OPERATING_SYSTEM_FAMILY_UNKNOWN
    if windows_locations.intersection(set(locations)):
        operating_system = definitions.OPERATING_SYSTEM_FAMILY_WINDOWS_NT
    elif '/system/library' in locations:
        operating_system = definitions.OPERATING_SYSTEM_FAMILY_MACOS
    elif '/etc' in locations:
        operating_system = definitions.OPERATING_SYSTEM_FAMILY_LINUX
    return operating_system