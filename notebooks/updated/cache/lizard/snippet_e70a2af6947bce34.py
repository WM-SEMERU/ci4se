def request_token(self, board):
    nonce = str(uuid.uuid4())
    data = {'scopes': 'write', 'client_id': self.client_id,
        'application_name': 'HelpMe', 'public_key': self.public_key.replace
        ("'", ''), 'nonce': nonce}
    url = (board +
        '/user-api-key/new?scopes=write&application_name=HelpMe&public_key=' +
        self.public_key.replace("'", '') + '&client_id=' + self.client_id +
        '&nonce=' + nonce)
    bot.newline()
    bot.info('Open browser to:')
    bot.info(url)
    bot.newline()
    bot.info('Copy paste token, press Ctrl-D to save it:')
    lines = []
    while True:
        try:
            line = enter_input()
        except EOFError:
            break
        if line:
            lines.append(line)
    message = '\n'.join(lines)
    tmpfile = mktemp()
    with open(tmpfile, 'w') as filey:
        filey.write(message)
    with open(tmpfile, 'rb') as filey:
        message = filey.read()
    cipher = Cipher_PKCS1_v1_5.new(self.key)
    decrypted = json.loads(cipher.decrypt(b64decode(message), None).decode())
    if 'nonce' not in decrypted:
        bot.exit('Missing nonce field in response for token, invalid.')
    if decrypted['nonce'] != nonce:
        bot.exit('Invalid nonce, exiting.')
    return decrypted['key']