def open(self, visible=False):
    if self.client:
        raise MatlabConnectionError(
            'Matlab(TM) COM client is still active. Use close to close it')
    self.client = win32com.client.Dispatch('matlab.application')
    self.client.visible = visible