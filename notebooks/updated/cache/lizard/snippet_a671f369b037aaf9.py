def importGenome(name, batchSize=100):
    path = os.path.join(this_dir, 'bootstrap_data', 'genomes/' + name)
    PG.importGenome(path, batchSize)