def get_element_id(self, complete_name):
    [group, name] = complete_name.split('.')
    element = self.get_element(group, name)
    if element:
        return element.ident
    else:
        logger.warning('Unable to find variable [%s]', complete_name)
        return None