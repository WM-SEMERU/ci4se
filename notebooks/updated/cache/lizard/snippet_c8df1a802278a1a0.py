def cli():
    objcli = WrHierCli(sys.argv[1:])
    fouts_txt = objcli.get_fouts()
    if fouts_txt:
        for fout_txt in fouts_txt:
            objcli.wrtxt_hier(fout_txt)
    else:
        objcli.prt_hier(sys.stdout)