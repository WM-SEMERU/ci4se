async def run(*cmd):
    stdout = await checked_run(*cmd)
    log_path = os.path.join(FLAGS.base_dir, get_cmd_name(cmd) + '.log')
    with gfile.Open(log_path, 'a') as f:
        f.write(expand_cmd_str(cmd))
        f.write('\n')
        f.write(stdout)
        f.write('\n')
    return stdout.split('\n')