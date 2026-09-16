def _clones(self):
    vbox = VirtualBox()
    machines = []
    for machine in vbox.machines:
        if machine.name == self.machine_name:
            continue
        if machine.name.startswith(self.machine_name):
            machines.append(machine)
    return machines