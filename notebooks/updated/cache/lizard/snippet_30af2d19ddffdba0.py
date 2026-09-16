def checkArgs(args):
    if not os.path.isfile(args.file):
        msg = '%s: no such file' % args.file
        raise ProgramError(msg)
    if args.population_file is None:
        msg = 'population-file: no population file'
        raise ProgramError(msg)
    elif not os.path.isfile(args.population_file):
        msg = '%s: no such file' % args.population_file
        raise ProgramError(msg)
    return True