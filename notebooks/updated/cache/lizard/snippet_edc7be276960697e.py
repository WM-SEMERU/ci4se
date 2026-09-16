def write_proc_sh(self):
    print('Writing proc.sh')
    context = {'tmp': '/tmp', 'home': '/app', 'settings': '/settings.yaml',
        'envsh': '/env.sh', 'port': self.config.port, 'cmd': self.get_cmd()}
    sh_path = os.path.join(get_container_path(self.config), 'proc.sh')
    rendered = get_template('proc.sh') % context
    with open(sh_path, 'w') as f:
        f.write(rendered)
    st = os.stat(sh_path)
    os.chmod(sh_path, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)