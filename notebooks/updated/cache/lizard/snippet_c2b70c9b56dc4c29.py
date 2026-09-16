def check_ups_input_frequency(the_session, the_helper, the_snmp_value):
    a_frequency = calc_frequency_from_snmpvalue(the_snmp_value)
    the_helper.add_metric(label=the_helper.options.type, value=a_frequency,
        uom='Hz')
    the_helper.set_summary('Input Frequency is {} Hz'.format(a_frequency))