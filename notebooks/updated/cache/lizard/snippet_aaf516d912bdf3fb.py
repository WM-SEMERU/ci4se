def imageplot(f, str=None, sbpt=None):
    if str is None:
        str = ''
    if sbpt is None:
        sbpt = []
    if sbpt != []:
        plt.subplot(sbpt[0], sbpt[1], sbpt[2])
    imgplot = plt.imshow(f, interpolation='nearest')
    imgplot.set_cmap('gray')
    plt.axis('off')
    if str != '':
        plt.title(str)