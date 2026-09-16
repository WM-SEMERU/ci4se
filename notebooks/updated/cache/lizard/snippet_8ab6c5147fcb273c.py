def variables(self):
    string = str(self)
    constants = [match[1:-1] for match in re.findall('{{[A-z0-9]}}', string)]
    variables = re.findall('{[A-z0-9]*}', string)
    return sorted(set(variables).difference(constants))