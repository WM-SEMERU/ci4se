def save_setup_command(argv, build_path):
    file_name = os.path.join(build_path, 'setup_command')
    with open(file_name, 'w') as f:
        f.write(' '.join(argv[:]) + '\n')