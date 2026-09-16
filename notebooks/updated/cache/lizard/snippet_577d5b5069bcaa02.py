def list_remotes(device=None, address=None):
    output = _call(['list', '', ''], None, device, address)
    remotes = [l.split()[-1] for l in output.splitlines() if l]
    return remotes