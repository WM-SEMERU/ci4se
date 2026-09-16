def validate_qparams(self):
    if isinstance(self, ShellAdapter):
        return
    err_msg = ''
    for param in self.qparams:
        if param not in self.supported_qparams:
            err_msg += 'Unsupported QUEUE parameter name %s\n' % param
            err_msg += 'Supported parameters:\n'
            for param_sup in self.supported_qparams:
                err_msg += '    %s \n' % param_sup
    if err_msg:
        raise ValueError(err_msg)