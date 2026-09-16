def write_ensemble(ensemble, options):
    size = len(ensemble)
    filename = '%s_%s_queries.csv' % (options.outname, size)
    file = os.path.join(os.getcwd(), filename)
    f = open(file, 'w')
    out = ', '.join(ensemble)
    f.write(out)
    f.close()