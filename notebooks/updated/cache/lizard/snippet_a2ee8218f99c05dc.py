def get_declared_envs(ini):
    tox_section_name = 'tox:tox' if ini.path.endswith('setup.cfg') else 'tox'
    tox_section = ini.sections.get(tox_section_name, {})
    envlist = split_env(tox_section.get('envlist', []))
    section_envs = [section[8:] for section in sorted(ini.sections, key=ini
        .lineof) if section.startswith('testenv:')]
    return envlist + [env for env in section_envs if env not in envlist]