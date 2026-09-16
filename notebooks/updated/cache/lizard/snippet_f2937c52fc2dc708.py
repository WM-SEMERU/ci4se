def configGet(self, vartype, category, name, optional=False,
    specialReturnMessage=None):
    try:
        if vartype == 'float':
            var = self.config.getfloat(category, name)
        elif vartype == 'string' or vartype == 'str':
            var = self.config.get(category, name)
            if var == '' and optional == False:
                if name[:17] != 'BoundaryCondition':
                    if self.Quiet != True:
                        print(
                            'An empty input string here is not an acceptable option.'
                            )
                        print(name, 'is not optional.')
                        print('Program crash likely to occur.')
        elif vartype == 'integer' or vartype == 'int':
            var = self.config.getint(category, name)
        elif vartype == 'boolean' or vartype == 'bool':
            var = self.config.getboolean(category, name)
        else:
            print(
                "Please enter 'float', 'string' (or 'str'), 'integer' (or 'int'), or 'boolean (or 'bool') for vartype"
                )
            sys.exit()
        return var
    except:
        if optional:
            var = None
            if self.Verbose or self.Debug:
                if self.grass == False:
                    print('')
                    print('No value entered for optional parameter "' +
                        name + '"')
                    print('in category "' + category +
                        '" in configuration file.')
                    print(
                        'No action related to this optional parameter will be taken.'
                        )
                    print('')
        else:
            print('Problem loading ' + vartype + ' "' + name +
                '" in category "' + category + '" from configuration file.')
            if specialReturnMessage:
                print(specialReturnMessage)
            sys.exit('Exiting.')