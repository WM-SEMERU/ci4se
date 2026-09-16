def cmd_config_show(option, show_keys):
    habucfg = loadcfg()
    if not show_keys:
        for key in habucfg.keys():
            if 'KEY' in key:
                habucfg[key] = '*************'
    print(json.dumps(habucfg, indent=4, sort_keys=True, default=str))