def _write_vmx_file(self):
    try:
        self.manager.write_vmx_file(self._vmx_path, self._vmx_pairs)
    except OSError as e:
        raise VMwareError('Could not write VMware VMX file "{}": {}'.format
            (self._vmx_path, e))