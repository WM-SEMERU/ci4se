def auto_doc(tool, nco_self):

    def desc(func):
        func.__doc__ = nco_self.call([tool, '--help']).get('stdout')
        return func
    return desc