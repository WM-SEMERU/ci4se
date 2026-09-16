def magphase_databoxes(ds, xscript=0, yscript='d[1]+1j*d[2]', eyscript=None,
    exscript=None, g=None, **kwargs):
    databoxes(ds, xscript, yscript, eyscript, exscript, plotter=
        magphase_data, g=g, **kwargs)