def main():
    args = sys.argv
    if '-h' in args:
        print(main.__doc__)
        sys.exit()
    dir_path = pmag.get_named_arg('-WD', '.')
    fmt = pmag.get_named_arg('-fmt', 'svg')
    save_plots = False
    interactive = True
    if '-sav' in sys.argv:
        save_plots = True
        interactive = False
    infile = pmag.get_named_arg('-f', 'specimens.txt')
    ipmag.dayplot_magic(dir_path, infile, save=save_plots, fmt=fmt,
        interactive=interactive)