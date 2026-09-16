def find_known_dependencies(self, requirement):
    logger.info('Checking for known dependencies of %s ..', requirement.name)
    known_dependencies = sorted(self.dependencies.get(requirement.name.
        lower(), []))
    if known_dependencies:
        logger.info('Found %s: %s', pluralize(len(known_dependencies),
            'known dependency', 'known dependencies'), concatenate(
            known_dependencies))
    else:
        logger.info('No known dependencies... Maybe you have a suggestion?')
    return known_dependencies