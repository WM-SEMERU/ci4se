def Validate(self):
    if not self.check_id:
        raise DefinitionError('Check has missing check_id value')
    cls_name = self.check_id
    if not self.method:
        raise DefinitionError('Check %s has no methods' % cls_name)
    ValidateMultiple(self.method, 'Check %s has invalid method definitions' %
        cls_name)