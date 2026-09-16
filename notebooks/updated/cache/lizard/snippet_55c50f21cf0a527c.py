def parse_config(contents):
    for identity_str, curve_name in re.findall('\\<(.*?)\\|(.*?)\\>', contents
        ):
        yield device.interface.Identity(identity_str=identity_str,
            curve_name=curve_name)