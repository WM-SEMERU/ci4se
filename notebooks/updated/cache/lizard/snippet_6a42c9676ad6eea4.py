def cli_wrapper(generator):
    first = True
    response = None
    while True:
        if not first:
            print()
        first = False
        try:
            message = generator.send(response)
            if isinstance(message, MultipleChoice):
                print(message.question)
                for num, choice in enumerate(message.options):
                    print('    {}: {}'.format(num, choice))
                option = input('Select an option 0-{}{}: '.format(len(
                    message.options) - 1, ' (default: {})'.format(message.
                    default) if message.default is not None else ''))
                if option == '' and message.default is not None:
                    option = message.default
                try:
                    response = int(option)
                except ValueError:
                    response = -1
                if not 0 <= response < len(message.options):
                    print('ERROR: {} is not a valid option.'.format(option))
                    return None
            elif isinstance(message, Text):
                print(message.question)
                response = input('> ')
            elif isinstance(message, Prompt):
                print(message.message)
                input('<Press enter to continue>')
                response = None
            elif isinstance(message, Info):
                print(message.message)
                response = None
        except Failure as f:
            print('ERROR: {}'.format(str(f)))
            return None
        except Success as s:
            return s.data