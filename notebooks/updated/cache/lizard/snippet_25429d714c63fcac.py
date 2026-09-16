def get_token_from_env():
    token = os.getenv('VAULT_TOKEN')
    if not token:
        token_file_path = os.path.expanduser('~/.vault-token')
        if os.path.exists(token_file_path):
            with open(token_file_path, 'r') as f_in:
                token = f_in.read().strip()
    if not token:
        return None
    return token