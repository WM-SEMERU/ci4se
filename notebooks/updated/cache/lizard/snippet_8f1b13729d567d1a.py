def generate_help(self):
    result = []
    result.append(self.__class__.__name__)
    result.append(re.sub('.', '=', self.__class__.__name__))
    result.append('')
    result.append('DESCRIPTION')
    result.append(self.description())
    result.append('')
    result.append('OPTIONS')
    opts = sorted(self.config.keys())
    for opt in opts:
        result.append(opt)
        helpstr = self.help[opt]
        if helpstr is None:
            helpstr = '-missing help-'
        result.append('\t' + helpstr)
        result.append('')
    return '\n'.join(result)