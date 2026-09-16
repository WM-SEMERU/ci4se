def validate(self, postdata, user=None):
    clam.common.util.printdebug('Validating inputtemplate ' + self.id + '...')
    errors, parameters, _ = processparameters(postdata, self.parameters, user)
    return errors, parameters