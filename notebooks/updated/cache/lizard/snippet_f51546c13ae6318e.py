def delif(self, iname):
    _runshell([brctlexe, 'delif', self.name, iname], 
        'Could not delete interface %s from %s.' % (iname, self.name))