def distribute_javaclasses(self, javaclass_dir, dest_dir='src'):
    info('Copying java files')
    ensure_dir(dest_dir)
    for filename in glob.glob(javaclass_dir):
        shprint(sh.cp, '-a', filename, dest_dir)