def main(args, options, parser):
    from spython.main.parse import DockerRecipe, SingularityRecipe
    if not args.files:
        parser.print_help()
        sys.exit(1)
    outfile = None
    if len(args.files) > 1:
        outfile = args.files[1]
    parser = SingularityRecipe
    if args.input == 'docker':
        parser = DockerRecipe
    elif args.input == 'singularity':
        parser = SingularityRecipe(args.files[0])
    elif 'dockerfile' in args.files[0].lower():
        parser = DockerRecipe
    parser = parser(args.files[0])
    entrypoint = '/bin/bash'
    force = False
    if args.entrypoint is not None:
        entrypoint = args.entrypoint
        force = True
    if outfile is not None:
        parser.save(outfile, runscript=entrypoint, force=force)
    else:
        recipe = parser.convert(runscript=entrypoint, force=True)
        print(recipe)