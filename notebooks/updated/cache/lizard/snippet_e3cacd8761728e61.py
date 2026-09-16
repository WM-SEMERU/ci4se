def save(self, filename, strip_prefix=''):
    arg_dict = {}
    for param in self.values():
        weight = param._reduce()
        if not param.name.startswith(strip_prefix):
            raise ValueError(
                "Prefix '%s' is to be striped before saving, but Parameter's name '%s' does not start with '%s'. this may be due to your Block shares parameters from other Blocks or you forgot to use 'with name_scope()' when creating child blocks. For more info on naming, please see http://mxnet.incubator.apache.org/tutorials/basic/naming.html"
                 % (strip_prefix, param.name, strip_prefix))
        arg_dict[param.name[len(strip_prefix):]] = weight
    ndarray.save(filename, arg_dict)