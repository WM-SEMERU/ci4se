def prt_paths(paths, prt=sys.stdout):
    pat = 'PATHES: {GO} L{L:02} D{D:02}\n'
    for path in paths:
        for go_obj in path:
            prt.write(pat.format(GO=go_obj.id, L=go_obj.level, D=go_obj.depth))
        prt.write('\n')