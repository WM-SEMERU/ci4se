def __preprocess_arguments(root):
    flags = ','.join(vsflags(VSFlags.UserValueRequired))
    arguments = root.getElementsByTagName('Argument')
    for argument in arguments:
        reference = __get_attribute(argument, 'Property')
        found = None
        for child in root.childNodes:
            if isinstance(child, Element):
                name = __get_attribute(child, 'Name')
                if name == reference:
                    found = child
                    break
        if found is not None:
            logging.info('Found property named %s', reference)
            switch = __get_attribute(argument.parentNode, 'Switch')
            if __get_attribute(found, 'Switch'):
                logging.debug('Copying node %s', reference)
                clone = found.cloneNode(True)
                root.insertBefore(clone, found)
                found = clone
            found.setAttribute('Switch', switch)
            found.setAttribute('Flags', flags)
        else:
            logging.warning('Could not find property named %s', reference)