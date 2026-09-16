def save():
    from .models import ModuleInfo
    logger = logging.getLogger(__name__)
    logger.info('Saving changes')
    for module in modules():
        if module.enabled:
            if module.changed:
                module.save()
                module.restart()
                module.commit()
            else:
                logger.debug('Not saving unchanged module: %s' % module.
                    verbose_name)
        else:
            logger.debug('Not saving disabled module: %s' % module.verbose_name
                )
    ModuleInfo.commit()
    logger.info('Changes saved')