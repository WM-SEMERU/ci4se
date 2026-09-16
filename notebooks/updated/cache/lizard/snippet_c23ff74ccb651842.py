def distribute_libs(self, arch, src_dirs, wildcard='*', dest_dir='libs'):
    info('Copying libs')
    tgt_dir = join(dest_dir, arch.arch)
    ensure_dir(tgt_dir)
    for src_dir in src_dirs:
        for lib in glob.glob(join(src_dir, wildcard)):
            shprint(sh.cp, '-a', lib, tgt_dir)