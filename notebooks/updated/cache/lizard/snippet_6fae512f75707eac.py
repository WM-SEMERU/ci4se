def create_poller(self, **kwargs):
    cacheablesource = createObject(kwargs['cacheablesource'].attrib[
        'factory'], kwargs['cacheablesource'])
    cachearea = createObject(kwargs['cachearea'].attrib['factory'], kwargs[
        'cachearea'])
    poll = abs(int(kwargs['cacheablesource'].attrib['poll']))
    logger.info(
        'Poller create for cacheablesource id %s and cachearea id %s' % (
        kwargs['cacheablesource'].attrib['id'], kwargs['cachearea'].attrib[
        'id']))
    return cacheablesource, cachearea, poll