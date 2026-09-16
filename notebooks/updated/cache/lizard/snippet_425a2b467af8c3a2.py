def initialize_pymol(options):
    import pymol
    pymol.finish_launching(args=['pymol', options, '-K'])
    pymol.cmd.reinitialize()