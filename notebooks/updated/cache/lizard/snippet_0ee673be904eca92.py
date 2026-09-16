def check_ups_alarms_present(the_session, the_helper, the_snmp_value):
    if the_snmp_value != '0':
        the_helper.add_status(pynag.Plugins.critical)
    else:
        the_helper.add_status(pynag.Plugins.ok)
    the_helper.set_summary('{} active alarms '.format(the_snmp_value))