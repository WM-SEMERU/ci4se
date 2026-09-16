def mkdir_uchroot(dirpath, root='.'):
    from benchbuild.utils.uchroot import no_args, uretry
    uchroot = no_args()
    uchroot = uchroot['-E', '-A', '-C', '-w', '/', '-r']
    uchroot = uchroot[os.path.abspath(root)]
    uretry(uchroot['--', '/bin/mkdir', '-p', dirpath])