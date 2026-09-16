def makeBenchmarkRunner(path, args):

    def runner():
        return BenchmarkProcess.spawn(executable=sys.executable, args=[
            '-Wignore'] + args, path=path.path, env=os.environ)
    return runner