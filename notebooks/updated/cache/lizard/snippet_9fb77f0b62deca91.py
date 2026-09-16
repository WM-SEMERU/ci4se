def user_parse(data):
    yield 'id', data.get('id')
    yield 'username', data.get('username')
    yield 'discriminator', data.get('discriminator')
    yield 'picture', 'https://cdn.discordapp.com/avatars/{}/{}.png'.format(data
        .get('id'), data.get('avatar'))