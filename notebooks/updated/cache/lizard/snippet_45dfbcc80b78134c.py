def bowtie(sam, btd, f, r, u, opt, no_shrink, threads):
    bt2 = 'bowtie2 -x %s -p %s ' % (btd, threads)
    if f is not False:
        bt2 += '-1 %s -2 %s ' % (f, r)
    if u is not False:
        bt2 += '-U %s ' % u
    bt2 += opt
    if no_shrink is False:
        if f is False:
            bt2 += ' | shrinksam -u -k %s-shrunk.sam ' % sam
        else:
            bt2 += ' | shrinksam -k %s-shrunk.sam ' % sam
    else:
        bt2 += ' > %s.sam' % sam
    return bt2