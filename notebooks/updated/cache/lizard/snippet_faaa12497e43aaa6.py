def Run(self, unused_args):
    subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
        'Software\\Microsoft\\Windows NT\\CurrentVersion', 0, winreg.KEY_READ)
    install_date = winreg.QueryValueEx(subkey, 'InstallDate')
    self.SendReply(rdfvalue.RDFDatetime.FromSecondsSinceEpoch(install_date[0]))