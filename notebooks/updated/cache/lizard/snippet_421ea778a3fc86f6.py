def guess_github_repo():
    p = subprocess.run(['git', 'ls-remote', '--get-url', 'origin'], stdout=
        subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if p.stderr or p.returncode:
        return False
    url = p.stdout.decode('utf-8').strip()
    m = GIT_URL.fullmatch(url)
    if not m:
        return False
    return m.group(1)