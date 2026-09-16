def startIndyPool(**kwargs):
    print('Starting indy_pool ...')
    if containerIsRunning('indy_pool'):
        print('... already running')
        exit(0)
    else:
        container = getContainer('indy_pool')
        if container:
            container.remove(force=True)
    try:
        image = getImage(path='/src/indy-sdk', dockerfile=
            'ci/indy-pool.dockerfile', tag='indy_pool')
    except TypeError as exc:
        image = getImage(path='/vagrant/indy-sdk', dockerfile=
            'ci/indy-pool.dockerfile', tag='indy_pool')
    except:
        print(
            'Failed to find indy-pool.dockerfile in /vagrant/indy-sdk or /src/indy-sdk'
            )
    container = runContainer(image, ports={'9701/tcp': ('0.0.0.0', 9701),
        '9702/tcp': ('0.0.0.0', 9702), '9703/tcp': ('0.0.0.0', 9703),
        '9704/tcp': ('0.0.0.0', 9704), '9705/tcp': ('0.0.0.0', 9705),
        '9706/tcp': ('0.0.0.0', 9706), '9707/tcp': ('0.0.0.0', 9707),
        '9708/tcp': ('0.0.0.0', 9708)}, detach=True, name='indy_pool')
    print('...started')