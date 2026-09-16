def run_cli(self, cli, args=None, node_paths=None):
    cli_args = [cli]
    if args:
        cli_args.append('--')
        cli_args.extend(args)
    return self.run_command(args=cli_args, node_paths=node_paths)