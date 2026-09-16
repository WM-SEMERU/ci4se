def createCorrFile(outfile, arrlist, template):
    if os.path.isfile(outfile):
        os.remove(outfile)
        print("Removing old corr file: '{:s}'".format(outfile))
    with fits.open(template, memmap=False) as ftemplate:
        for arr in arrlist:
            ftemplate[arr['sciext']].data = arr['corrFile']
            if arr['dqext'][0] != arr['sciext'][0]:
                ftemplate[arr['dqext']].data = arr['dqMask']
        ftemplate.writeto(outfile)
        print("Created CR corrected file: '{:s}'".format(outfile))