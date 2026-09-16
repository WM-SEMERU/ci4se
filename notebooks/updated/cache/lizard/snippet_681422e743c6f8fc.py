def docker_run(ctx, docker_run_args, help):
    args = list(docker_run_args)
    if len(args) > 0 and args[0] == 'run':
        args.pop(0)
    if help or len(args) == 0:
        wandb.termlog(
            'This commands adds wandb env variables to your docker run calls')
        subprocess.call(['docker', 'run'] + args + ['--help'])
        exit()
    if len([a for a in args if a.startswith('--runtime')]
        ) == 0 and find_executable('nvidia-docker'):
        args = ['--runtime', 'nvidia'] + args
    image = util.image_from_docker_args(args)
    resolved_image = None
    if image:
        resolved_image = wandb.docker.image_id(image)
    if resolved_image:
        args = ['-e', 'WANDB_DOCKER=%s' % resolved_image] + args
    else:
        wandb.termlog(
            "Couldn't detect image argument, running command without the WANDB_DOCKER env variable"
            )
    if api.api_key:
        args = ['-e', 'WANDB_API_KEY=%s' % api.api_key] + args
    else:
        wandb.termlog(
            'Not logged in, run `wandb login` from the host machine to enable result logging'
            )
    subprocess.call(['docker', 'run'] + args)