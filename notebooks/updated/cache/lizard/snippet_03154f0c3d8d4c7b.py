def run(self):
    self.announce('Moving library files', level=3)
    self.skip_build = True
    bin_dir = self.distribution.bin_dir
    libs = [os.path.join(bin_dir, _lib) for _lib in os.listdir(bin_dir) if 
        os.path.isfile(os.path.join(bin_dir, _lib)) and os.path.splitext(
        _lib)[1] in ['.dll', '.so'] and not (_lib.startswith('python') or
        _lib.startswith('bpy'))]
    for lib in libs:
        shutil.move(lib, os.path.join(self.build_dir, os.path.basename(lib)))
    self.distribution.data_files = [os.path.join(self.install_dir, os.path.
        basename(lib)) for lib in libs]
    self.distribution.run_command('install_data')
    super().run()