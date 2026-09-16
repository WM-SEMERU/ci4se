def unpack_sver_response_version(packet):
    software_name = packet.data.decode('utf-8')
    legacy_version_field = packet.arg2 >> 16
    if legacy_version_field != 65535:
        major = legacy_version_field // 100
        minor = legacy_version_field % 100
        patch = 0
        labels = ''
    else:
        software_name, _, version_number = software_name.partition('\x00')
        match = VERSION_NUMBER_REGEX.match(version_number.rstrip('\x00'))
        assert match, 'Malformed version number: {}'.format(version_number)
        major = int(match.group(1))
        minor = int(match.group(2))
        patch = int(match.group(3))
        labels = match.group(4) or ''
    return software_name.rstrip('\x00'), (major, minor, patch), labels