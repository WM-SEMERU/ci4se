def remove_rich_rule(zone, rule, permanent=True):
    cmd = "--zone={0} --remove-rich-rule='{1}'".format(zone, rule)
    if permanent:
        cmd += ' --permanent'
    return __firewall_cmd(cmd)