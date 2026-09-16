def remove_diagnostic(self, name):
    try:
        delattr(self, name)
        self._diag_vars.remove(name)
    except:
        print('No diagnostic named {} was found.'.format(name))