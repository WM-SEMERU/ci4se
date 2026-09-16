def samba():
    username = env.user
    install_packages(['samba'])
    run(flo('sudo smbpasswd -a {username}'))
    path = '$HOME/shared'
    sharename = 'shared'
    comment = '"smb share; everyone has full access (read/write)"'
    acl = flo('Everyone:F,{username}:F guest_ok=y')
    with warn_only():
        run(flo('mkdir {path}'))
    run(flo('sudo net usershare add {sharename} {path} {comment} {acl}'))
    run(flo('sudo net usershare info {sharename}'))