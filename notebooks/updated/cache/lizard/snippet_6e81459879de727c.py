def dcm2nii(dcmpth, fimout='', fprefix='converted-from-DICOM_', fcomment='',
    outpath='', timestamp=True, executable='', force=False):
    if os.path.isfile(fimout) and not force:
        return fimout
    if executable == '':
        try:
            import resources
            executable = resources.DCM2NIIX
        except:
            raise NameError(
                'e> could not import resources                     or find variable DCM2NIIX in resources.py'
                )
    elif not os.path.isfile(executable):
        raise IOError('e> the executable is incorrect!')
    if not os.path.isdir(dcmpth):
        raise IOError('e> the provided DICOM path is not a folder!')
    if outpath == '' and fimout != '' and '/' in fimout:
        opth = os.path.dirname(fimout)
        if opth == '':
            opth = dcmpth
        fimout = os.path.basename(fimout)
    elif outpath == '':
        opth = dcmpth
    else:
        opth = outpath
    create_dir(opth)
    if fimout == '':
        fimout = fprefix
        if timestamp:
            fimout += time_stamp(simple_ascii=True)
    fimout = fimout.split('.nii')[0]
    call([executable, '-f', fimout, '-o', opth, dcmpth])
    fniiout = glob.glob(os.path.join(opth, '*' + fimout + '*.nii*'))
    if fniiout:
        return fniiout[0]
    else:
        raise ValueError('e> could not get the output file!')