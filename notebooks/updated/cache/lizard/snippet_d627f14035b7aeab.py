def get_sys():
    cmd = ''
    if salt.utils.path.which('localectl'):
        cmd = 'localectl | grep Keymap | sed -e"s/: /=/" -e"s/^[ \t]*//"'
    elif 'RedHat' in __grains__['os_family']:
        cmd = 'grep LAYOUT /etc/sysconfig/keyboard | grep -vE "^#"'
    elif 'Debian' in __grains__['os_family']:
        cmd = 'grep XKBLAYOUT /etc/default/keyboard | grep -vE "^#"'
    elif 'Gentoo' in __grains__['os_family']:
        cmd = 'grep "^keymap" /etc/conf.d/keymaps | grep -vE "^#"'
    out = __salt__['cmd.run'](cmd, python_shell=True).split('=')
    ret = out[1].replace('"', '')
    return ret