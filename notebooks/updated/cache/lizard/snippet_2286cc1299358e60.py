def check_whitelist(values):
    import os
    import tldextract
    whitelisted = list()
    for name in ['alexa.txt', 'cisco.txt']:
        config_path = os.path.expanduser('~/.config/blockade')
        file_path = os.path.join(config_path, name)
        whitelisted += [x.strip() for x in open(file_path, 'r').readlines()]
    output = list()
    for item in values:
        ext = tldextract.extract(item)
        if ext.registered_domain in whitelisted:
            continue
        output.append(item)
    return output