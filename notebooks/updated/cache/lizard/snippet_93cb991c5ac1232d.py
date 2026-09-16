def startup_script(self):
    script_file = self.script_file
    if script_file is None:
        return None
    try:
        with open(script_file, 'rb') as f:
            return f.read().decode('utf-8', errors='replace')
    except OSError as e:
        raise VPCSError('Cannot read the startup script file "{}": {}'.
            format(script_file, e))