def _getJavaStorageLevel(self, storageLevel):
    if not isinstance(storageLevel, StorageLevel):
        raise Exception('storageLevel must be of type pyspark.StorageLevel')
    newStorageLevel = self._jvm.org.apache.spark.storage.StorageLevel
    return newStorageLevel(storageLevel.useDisk, storageLevel.useMemory,
        storageLevel.useOffHeap, storageLevel.deserialized, storageLevel.
        replication)