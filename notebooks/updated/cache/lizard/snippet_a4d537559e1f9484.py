def list_containers(self):
    data = run_cmd(['machinectl', 'list', '--no-legend', '--no-pager'],
        return_output=True)
    output = []
    reg = re.compile('\\s+')
    for line in data.split('\n'):
        stripped = line.strip()
        if stripped:
            parts = reg.split(stripped)
            name = parts[0]
            output.append(self.ContainerClass(None, None, name=name))
    return output