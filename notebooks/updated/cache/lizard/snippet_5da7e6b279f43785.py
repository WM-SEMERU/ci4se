def main(items=None, printmd=None, printcal=False, found=False, save=None,
    download=None, requestor_pays=False, **kwargs):
    if items is None:
        search = Search.search(**kwargs)
        if found:
            num = search.found()
            print('%s items found' % num)
            return num
        items = search.items()
    else:
        items = Items.load(items)
    print('%s items found' % len(items))
    if printmd is not None:
        print(items.summary(printmd))
    if printcal:
        print(items.calendar())
    if save is not None:
        items.save(filename=save)
    if download is not None:
        if 'ALL' in download:
            download = set([k for i in items for k in i.assets])
        for key in download:
            items.download(key=key, path=config.DATADIR, filename=config.
                FILENAME, requestor_pays=requestor_pays)
    return items