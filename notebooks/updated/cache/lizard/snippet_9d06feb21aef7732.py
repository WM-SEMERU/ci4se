def download_message(self):
    print('Failed to find any ImageNet %s files' % self.subset)
    print('')
    print(
        """If you have already downloaded and processed the data, then make sure to set --data_dir to point to the directory containing the location of the sharded TFRecords.
"""
        )
    print(
        """If you have not downloaded and prepared the ImageNet data in the TFRecord format, you will need to do this at least once. This process could take several hours depending on the speed of your computer and network connection
"""
        )
    print(
        """Please see README.md for instructions on how to build the ImageNet dataset using download_and_preprocess_imagenet.
"""
        )
    print(
        'Note that the raw data size is 300 GB and the processed data size is 150 GB. Please ensure you have at least 500GB disk space.'
        )