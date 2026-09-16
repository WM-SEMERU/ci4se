def openRtpPort(self):
    self.rtpSocket.settimeout(0.5)
    try:
        self.rtpSocket.bind((self.serverAddr, self.rtpPort))
        print('Bind RtpPort Success')
    except:
        tkinter.messagebox.showwarning('Connection Failed',
            'Connection to rtpServer failed...')