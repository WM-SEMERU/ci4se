def main():
    options = optionsParser().parse_args()
    params = getSelectionParams(options)
    if options.list or options.details:
        specifiedMaps = filterMapNames(options.mapname, records=
            filterMapAttrs(**params), excludeRegex=options.exclude,
            closestMatch=options.best)
        if specifiedMaps:
            for v in specifiedMaps:
                if options.details:
                    v.display()
                else:
                    print(v)
            print('Found %d maps that match given criteria.' % len(
                specifiedMaps))
        else:
            print('No matching maps found.')
    else:
        try:
            specifiedMaps = selectMap(options.mapname, excludeName=options.
                exclude, closestMatch=options.best, **params)
        except Exception as e:
            specifiedMaps = []
            print('No matching maps found: %s' % e)
        if not isinstance(specifiedMaps, list):
            specifiedMaps = [specifiedMaps]
        for m in specifiedMaps:
            if options.path:
                print(m.path)
            else:
                print(m.name)