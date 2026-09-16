def get_decompression_transform_files(self, offset=0):
    compression_algorithm, _, _ = self.compression_details
    return [{'algorithm': algorithm, 'order': str(index + offset + 1),
        'type': 'decompression'} for index, algorithm in enumerate(
        compression_algorithm.split(','))]