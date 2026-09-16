def HiResHDU(model):
    cards = model._mission.HDUCards(model.meta, hdu=5)
    cards.append(('COMMENT', '************************'))
    cards.append(('COMMENT', '*     EVEREST INFO     *'))
    cards.append(('COMMENT', '************************'))
    cards.append(('MISSION', model.mission, 'Mission name'))
    cards.append(('VERSION', EVEREST_MAJOR_MINOR, 'EVEREST pipeline version'))
    cards.append(('SUBVER', EVEREST_VERSION, 'EVEREST pipeline subversion'))
    cards.append(('DATE', strftime('%Y-%m-%d'),
        'EVEREST file creation date (YYYY-MM-DD)'))
    header = pyfits.Header(cards=cards)
    if model.hires is not None:
        hdu = pyfits.ImageHDU(data=model.hires, header=header, name=
            'HI RES IMAGE')
    else:
        hdu = pyfits.ImageHDU(data=np.empty((0, 0), dtype=float), header=
            header, name='HI RES IMAGE')
    return hdu