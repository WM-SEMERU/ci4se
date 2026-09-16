def FrameworkDir64(self):
    guess_fw = os.path.join(self.WinDir, 'Microsoft.NET\\Framework64')
    return self.ri.lookup(self.ri.vc, 'frameworkdir64') or guess_fw