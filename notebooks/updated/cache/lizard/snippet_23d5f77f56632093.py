def generate_authors(git_dir):
    authors = []
    emails = []
    git_log_cmd = ['git', 'log', '--format=%aN|%aE']
    tmp_authors = _run_shell_command(git_log_cmd, git_dir).split('\n')
    for author_str in tmp_authors:
        author, email = author_str.split('|')
        author = author.strip()
        email = email.strip()
        if author.lower() not in [x.lower() for x in authors]:
            if email.lower() not in [x.lower() for x in emails]:
                authors.append(author)
                emails.append(email)
    co_authors_raw = _run_shell_command(['git', 'log'], git_dir)
    co_authors = re.findall('Co-authored-by:.+', co_authors_raw, re.MULTILINE)
    co_authors = [signed.split(':', 1)[1].strip().split('<') for signed in
        co_authors if signed]
    for author_str in co_authors:
        author, email = author_str.split('<')
        author = author.strip()
        email = email[:-1].strip()
        if author.lower() not in [x.lower() for x in authors]:
            if email.lower() not in [x.lower() for x in emails]:
                authors.append(author)
                emails.append(email)
    authors = sorted(set(authors))
    return authors