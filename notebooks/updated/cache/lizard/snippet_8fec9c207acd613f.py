def from_args(cls, args):
    confFiles = []
    if args.config_files:
        confFiles += args.config_files
    confDeletes = args.config_delete or []
    parsedDeletes = []
    for delete in confDeletes:
        splitDelete = delete.split(':')
        if len(splitDelete) > 2:
            raise ValueError(
                'Deletes must be of format section:option or section. Cannot parse %s.'
                 % str(delete))
        else:
            parsedDeletes.append(tuple(splitDelete))
    confOverrides = args.config_overrides or []
    parsedOverrides = []
    for override in confOverrides:
        splitOverride = override.split(':')
        if len(splitOverride) == 3:
            parsedOverrides.append(tuple(splitOverride))
        elif len(splitOverride) == 2:
            parsedOverrides.append(tuple(splitOverride + ['']))
        elif len(splitOverride) > 3:
            rec_value = ':'.join(splitOverride[2:])
            parsedOverrides.append(tuple(splitOverride[:2] + [rec_value]))
        else:
            raise ValueError(
                'Overrides must be of format section:option:value or section:option. Cannot parse %s.'
                 % str(override))
    return cls(confFiles, parsedOverrides, None, parsedDeletes)