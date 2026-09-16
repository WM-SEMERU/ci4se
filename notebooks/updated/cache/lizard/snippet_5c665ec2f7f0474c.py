def _CompileProtos():
    proto_files = []
    for dir_path, _, filenames in os.walk(THIS_DIRECTORY):
        for filename in filenames:
            if filename.endswith('.proto'):
                proto_files.append(os.path.join(dir_path, filename))
    if not proto_files:
        return
    protoc_command = ['python', '-m', 'grpc_tools.protoc', '--python_out',
        THIS_DIRECTORY, '--grpc_python_out', THIS_DIRECTORY, '--proto_path',
        THIS_DIRECTORY]
    protoc_command.extend(proto_files)
    subprocess.check_output(protoc_command)