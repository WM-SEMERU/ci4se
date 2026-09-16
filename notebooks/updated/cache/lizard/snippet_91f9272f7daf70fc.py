def compute_eigenvalues(in_prefix, out_prefix):
    with open(out_prefix + '.parameters', 'w') as o_file:
        print >> o_file, 'genotypename:    ' + in_prefix + '.bed'
        print >> o_file, 'snpname:         ' + in_prefix + '.bim'
        print >> o_file, 'indivname:       ' + in_prefix + '.fam'
        print >> o_file, 'evecoutname:     ' + out_prefix + '.evec.txt'
        print >> o_file, 'evaloutname:     ' + out_prefix + '.eval.txt'
        print >> o_file, 'numoutlieriter:  0'
        print >> o_file, 'altnormstyle:    NO'
    command = ['smartpca', '-p', out_prefix + '.parameters']
    runCommand(command)