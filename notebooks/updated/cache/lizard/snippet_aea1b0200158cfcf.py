def state(self, value):
    if value.upper() == ON:
        return self.SOAPAction('SetSocketSettings',
            'SetSocketSettingsResult', self.controlParameters('1', 'true'))
    elif value.upper() == OFF:
        return self.SOAPAction('SetSocketSettings',
            'SetSocketSettingsResult', self.controlParameters('1', 'false'))
    else:
        raise TypeError('State %s is not valid.' % str(value))