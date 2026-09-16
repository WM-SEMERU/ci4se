def populate_device(dev):
    try:
        tgt = PackTargets._generate_pack_target_class(dev)
        if tgt is None:
            return
        part = dev.part_number.lower()
        LOG.debug("Loading target '%s' from CMSIS-Pack", part)
        if part not in TARGET:
            TARGET[part] = tgt
    except (MalformedCmsisPackError, FileNotFoundError_) as err:
        LOG.warning(err)