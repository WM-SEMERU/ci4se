def push(self, remote, branch=None):
    pb = ProgressBar()
    pb.setup(self.name, ProgressBar.Action.PUSH)
    if branch:
        result = remote.push(branch, progress=pb)
    else:
        result = remote.push(progress=pb)
    print()
    return result, pb.other_lines