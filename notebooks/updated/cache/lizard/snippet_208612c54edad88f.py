def find_serial_devices(serial_matcher='ED'):
    objWMIService = win32com.client.Dispatch('WbemScripting.SWbemLocator')
    objSWbemServices = objWMIService.ConnectServer('.', 'root\\cimv2')
    items = objSWbemServices.ExecQuery(
        'SELECT * FROM Win32_USBControllerDevice')
    ids = (item.Dependent.strip('"')[-8:] for item in items)
    return [e for e in ids if e.startswith(serial_matcher)]