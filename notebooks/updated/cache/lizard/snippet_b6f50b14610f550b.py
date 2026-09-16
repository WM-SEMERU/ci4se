def cc_run(args):
    prog = b'int main(){}\n'
    pipe = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.
        PIPE, close_fds=True)
    pipe.communicate(input=prog)
    if os.WIFEXITED(pipe.returncode):
        return os.WEXITSTATUS(pipe.returncode) == 0
    return False