def get_libgfortran_dir():
    for ending in ['.3.dylib', '.dylib', '.3.so', '.so']:
        try:
            p = Popen(['gfortran', '-print-file-name=libgfortran' + ending],
                stdout=PIPE, stderr=PIPE)
            p.stderr.close()
            line = p.stdout.readline().decode().strip()
            p.stdout.close()
            if os.path.exists(line):
                return [os.path.dirname(line)]
        except:
            continue
        return []