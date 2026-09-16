def execute(self, correlation_id, command, args):
    cref = self.find_command(command)
    if cref == None:
        raise BadRequestException(correlation_id, 'CMD_NOT_FOUND',
            'Requested command does not exist').with_details('command', command
            )
    if correlation_id == None:
        correlation_id = IdGenerator.next_short()
    results = cref.validate(args)
    ValidationException.throw_exception_if_needed(correlation_id, results,
        False)
    return cref.execute(correlation_id, args)