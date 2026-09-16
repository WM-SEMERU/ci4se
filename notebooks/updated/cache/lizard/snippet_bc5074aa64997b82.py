def attribute_is_public(self, permission):
    try:
        parent = getattr(self, 'parent_{}'.format(permission))
        student = getattr(self, 'self_{}'.format(permission))
        return parent and student
    except Exception:
        logger.error('Could not retrieve permissions for {}'.format(permission)
            )