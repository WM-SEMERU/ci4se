def validate(self, value):
    if self.testFlag(self.Flags.Required) and not self.testFlag(self.Flags.
        AutoAssign):
        if self.isNull(value):
            msg = '{0} is a required column.'.format(self.name())
            raise orb.errors.ColumnValidationError(self, msg)
    return True