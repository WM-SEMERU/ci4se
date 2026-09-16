def as_string(self):
    if type(self.instruction) is str:
        return self.instruction
    if self.action == 'FROM' and not isinstance(self.command, six.string_types
        ):
        extra = '' if self.extra is NotSpecified else ' {0}'.format(self.extra)
        return '{0} {1}{2}'.format(self.action, self.command.from_name, extra)
    else:
        return '{0} {1}'.format(self.action, self.command)