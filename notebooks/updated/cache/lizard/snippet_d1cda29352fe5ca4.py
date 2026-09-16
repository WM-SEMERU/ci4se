def execute_add(args, root_dir=None):
    command = ' '.join(args['command'])
    instruction = {'command': command, 'path': os.getcwd()}
    print_command_factory('add')(instruction, root_dir)