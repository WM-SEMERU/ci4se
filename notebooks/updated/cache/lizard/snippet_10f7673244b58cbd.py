def print_whats_next(profile):
    what_next = [
        '{{autogreen}}Congratulations!{{/autogreen}} You are logged in to the MAAS server at {{autoblue}}{profile.url}{{/autoblue}} with the profile name {{autoblue}}{profile.name}{{/autoblue}}.'
        , 'For help with the available commands, try:', '  maas help']
    for message in what_next:
        message = message.format(profile=profile)
        print(colorized(message))
        print()