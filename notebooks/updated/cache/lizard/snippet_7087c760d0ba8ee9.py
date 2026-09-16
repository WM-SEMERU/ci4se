def make_stacker_cmd_string(args, lib_path):
    if platform.system().lower() == 'windows':
        lib_path = lib_path.replace('\\', '/')
    return (
        "import sys;sys.argv = ['stacker'] + {args};sys.path.insert(1, '{lib_path}');from stacker.logger import setup_logging;from stacker.commands import Stacker;stacker = Stacker(setup_logging=setup_logging);args = stacker.parse_args({args});stacker.configure(args);args.run(args)"
        .format(args=str(args), lib_path=lib_path))