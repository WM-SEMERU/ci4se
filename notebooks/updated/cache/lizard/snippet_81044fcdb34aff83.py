def nii_ugzip(imfile, outpath=''):
    import gzip
    with gzip.open(imfile, 'rb') as f:
        s = f.read()
    if outpath == '':
        fout = imfile[:-3]
    else:
        fout = os.path.join(outpath, os.path.basename(imfile)[:-3])
    with open(fout, 'wb') as f:
        f.write(s)
    return fout