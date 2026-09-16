def _get_tokens(morph_fd):
    for line in morph_fd:
        line = line.rstrip()
        line = line.split(';', 1)[0]
        squash_token = []
        if '<(' in line:
            assert ')>' in line, 'Missing end of spine'
            continue
        for token in line.replace('(', ' ( ').replace(')', ' ) ').split():
            if squash_token:
                squash_token.append(token)
                if token.endswith('"'):
                    token = ' '.join(squash_token)
                    squash_token = []
                    yield token
            elif token.startswith('"') and not token.endswith('"'):
                squash_token.append(token)
            else:
                yield token