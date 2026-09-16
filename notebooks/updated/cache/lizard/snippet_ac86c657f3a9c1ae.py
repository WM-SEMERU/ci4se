def create_objects(self, raw_objects):
    types_creations = self.__class__.types_creations
    early_created_types = self.__class__.early_created_types
    logger.info('Creating objects...')
    self.add_self_defined_objects(raw_objects)
    for o_type in sorted(types_creations):
        if o_type not in early_created_types:
            self.create_objects_for_type(raw_objects, o_type)
    logger.info('Done')