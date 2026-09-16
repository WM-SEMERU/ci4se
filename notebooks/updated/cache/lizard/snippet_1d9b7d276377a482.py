def patch_ironic_ramdisk(self):
    tmpdir = self.run('mktemp -d')[0].rstrip('\n')
    self.run(
        'cd {tmpdir}; zcat /home/stack/ironic-python-agent.initramfs| cpio -id'
        .format(tmpdir=tmpdir))
    self.send_file(pkg_data_filename('static', 'ironic-wipefs.patch'),
        '/tmp/ironic-wipefs.patch')
    self.run('cd {tmpdir}; patch -p0 < /tmp/ironic-wipefs.patch'.format(
        tmpdir=tmpdir))
    self.run(
        'cd {tmpdir}; find . | cpio --create --format=newc > /home/stack/ironic-python-agent.initramfs'
        .format(tmpdir=tmpdir))