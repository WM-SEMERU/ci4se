def health_check(self):
    output = 'Chassis Alarms:\n\t'
    chassis_alarms = self._session.command('show chassis alarms')
    chassis_alarms = chassis_alarms.xpath('//alarm-detail')
    system_alarms = self._session.command('show system alarms')
    system_alarms = system_alarms.xpath('//alarm-detail')
    chass = self._session.command(command='show chassis routing-engine',
        format='text').xpath('//output')[0].text
    proc = self._session.command('show system processes extensive')
    proc = proc.xpath('output')[0].text.split('\n')
    if chassis_alarms == []:
        output += 'No chassis alarms active.\n'
    else:
        for i in chassis_alarms:
            output += i.xpath('alarm-class')[0].text.strip(
                ) + ' Alarm \t\t' + i.xpath('alarm-time')[0].text.strip(
                ) + '\n\t' + i.xpath('alarm-description')[0].text.strip(
                ) + '\n'
    output += '\nSystem Alarms: \n\t'
    if system_alarms == []:
        output += 'No system alarms active.\n'
    else:
        for i in system_alarms:
            output += i.xpath('alarm-class')[0].text.strip(
                ) + ' Alarm \t\t' + i.xpath('alarm-time')[0].text.strip(
                ) + '\n\t' + i.xpath('alarm-description')[0].text.strip(
                ) + '\n'
    output += '\n' + chass
    output += (
        '\n\nTop 5 busiest processes (high mgd values likely from script execution):\n'
        )
    for line_number in range(8, 14):
        output += proc[line_number] + '\n'
    return output