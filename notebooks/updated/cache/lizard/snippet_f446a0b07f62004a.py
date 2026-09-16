def get_collections_data(self):
    collections = {'left': self.left_collection, 'right': self.right_collection
        }
    for collection_type, collection in collections.iteritems():
        pipeline = self.build_pipeline(collection)
        self.collections_data[collection_type] = self.fetch_and_process_data(
            collection, pipeline)