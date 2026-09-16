def check_indexes(self):
    for collection_name in INDEXES:
        existing_indexes = self.indexes(collection_name)
        indexes = INDEXES[collection_name]
        for index in indexes:
            index_name = index.document.get('name')
            if not index_name in existing_indexes:
                logger.warning('Index {0} missing. Run command `loqusdb index`'
                    .format(index_name))
                return
    logger.info('All indexes exists')